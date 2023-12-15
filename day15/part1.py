import aoc

import functools
import itertools
import math
import numpy
import re


def holiday_hash(s: str) -> int:
    return functools.reduce(lambda h, c: (((h + ord(c))) * 17) % 256, s, 0)


def holiday_hash_line(line):
    return sum(holiday_hash(s) for s in line.split(","))


def part1(input: list[str]) -> int:
    return holiday_hash_line(input[0])


if __name__ == "__main__":
    result = aoc.run_script(part1)
    print(f"Part 1: {result}")
