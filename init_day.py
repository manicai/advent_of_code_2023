import os
import pathlib as path

import requests

import aoc

standard_imports = """
import functools
import itertools
import math
import re
"""

part1_template = f"""import aoc
{standard_imports}

def part1(input):
    pass

def test():
    pass

if __name__ == "__main__":
    test()
    aoc.run_script(part1)
"""

part2_template = f"""import aoc
import part1
{standard_imports}

def part2(input):
    pass

def test():
    pass

if __name__ == "__main__":
    test()
    aoc.run_script(part2)
"""


                                
def download_tests(day=aoc.today(), year=aoc.year()):
    problem_url = f"https://adventofcode.com/{year}/day/{day}"
    problem_file = aoc.inputs_dir() / 'problem.html'
    if not problem_file.is_file():
        response = requests.get(problem_url)
        if not response.status_code == 200:
            print(f"Failed to get problem statement ({response.status_code}):", 
                response.text)
        else:
            with open(problem_file, 'w') as fh:
                fh.write(response.text)


if __name__ == "__main__":
    root = path.Path(os.environ['AOC_ROOT'])

    path.Path.mkdir(aoc.inputs_dir(), parents=True, exist_ok=True)
    aoc.download_input()
    download_tests()

    code_dir = path.Path(f"day{aoc.today():02}")
    path.Path.mkdir(code_dir, exist_ok=True)
    part1 = code_dir / "part1.py"
    if not part1.is_file():
        with open(part1, "w") as fh:
            fh.write(part1_template)
    else:
        print(f"Part 1 template {part1} already exists")

    part2 = code_dir / "part2.py"
    if not part2.is_file():
        with open(part2, "w") as fh:
            fh.write(part2_template)
    else:
        print(f"Part 2 template {part2} already exists")
