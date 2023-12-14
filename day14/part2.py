import aoc

# Horrid hack because I can't be bothered to think about paths and
# packages for this.
try:
    from . import part1
except ImportError:
    import part1

import functools
import itertools
import math
import numpy
import re


def part2(input: list[str]) -> int:
    pass


if __name__ == "__main__":
    result = aoc.run_script(part2)
    print(f"Part 2: {result}")
