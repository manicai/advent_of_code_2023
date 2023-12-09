import aoc
import part1

import functools
import itertools
import math
import numpy
import re


def part2(input):
    total = 0
    for line in input:
        values = list(reversed(aoc.to_ints(line.split())))
        new = part1.extrapolate(values)
        print(f"{line} -> {new}")
        total += new
    print("Total", total)
    return total


if __name__ == "__main__":
    aoc.run_script(part2)
