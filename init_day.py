import datetime
import os
import pathlib as path

import requests
import bs4

import aoc

standard_imports = """
import functools
import itertools
import math
import re
import numpy
"""

templates = {"__init__": ""}

templates[
    "part1"
] = f"""#!/usr/bin/env python3
\"\"\"Advent of Code {aoc.year()} Day {aoc.today()} Part 1\"\"\"
{standard_imports}

import aoc


def part1(input: list[str]) -> int:
    pass


if __name__ == "__main__":
    result = aoc.run_script(part1, day={aoc.today()})
    print(f"Part 1: {{result}}")
"""

templates[
    "part2"
] = f"""#!/usr/bin/env python3
\"\"\"Advent of Code {aoc.year()} Day {aoc.today()} Part 2\"\"\"
{standard_imports}

import aoc
import day{aoc.today()}.part1 as part1


def part2(input: list[str]) -> int:
    pass


if __name__ == "__main__":
    result = aoc.run_script(part2, day={aoc.today()})
    print(f"Part 2: {{result}}")
"""

test_template = f"""import pytest
from day{aoc.today()}.{{}} import *


def test():
    pass
"""

code_dir = path.Path(f"day{aoc.today():02}")


def download_tests(day=aoc.today(), year=aoc.year()):
    problem_url = f"https://adventofcode.com/{year}/day/{day}"
    problem_file = aoc.inputs_dir(day) / "problem.html"
    if not problem_file.is_file():
        response = requests.get(problem_url)
        if not response.status_code == 200:
            print(
                f"Failed to get problem statement ({response.status_code}):",
                response.text,
            )
        else:
            with open(problem_file, "w", encoding=response.encoding) as fh:
                fh.write(response.text)

    with open(problem_file, "r") as fh:
        soup = bs4.BeautifulSoup(fh, features="html.parser")

    if len(soup.main.find_all("pre")) == 1:
        with open(code_dir / "test.txt", "w") as fh:
            fh.write(soup.main.pre.text)
    else:
        for i, block in enumerate(soup.main.find_all("pre")):
            with open(code_dir / f"test_{i}.txt", "w", encoding="utf8") as fh:
                fh.write(block.text)


if __name__ == "__main__":
    assert datetime.datetime.now().month == 12, "Advent is in December"
    assert datetime.datetime.now().day <= 25

    root = path.Path(os.environ["AOC_ROOT"])

    path.Path.mkdir(aoc.inputs_dir(), parents=True, exist_ok=True)
    aoc.download_input()

    path.Path.mkdir(code_dir, exist_ok=True)
    download_tests()
    for part in templates:
        code_file = code_dir / f"{part}.py"
        if not code_file.is_file():
            with open(code_file, "w") as fh:
                fh.write(templates[part])
        else:
            print(f"Template {code_file} already exists")

        if templates[part]:
            test_file = code_dir / f"test_{part}.py"
            if not test_file.is_file():
                with open(test_file, "w") as fh:
                    fh.write(test_template.format(part))
            else:
                print(f"Test template {test_file} already exists")
