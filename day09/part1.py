import aoc

import functools
import itertools
import math
import numpy
import re


def extrapolate(seq) -> int:
    if not any(seq):
        return 0
    return seq[-1] + extrapolate(list(y - x for x, y in itertools.pairwise(seq)))


def part1(input):
    total = 0
    for line in input:
        values = aoc.to_ints(line.split())
        new = extrapolate(values)
        print(f"{line} -> {new}")
        total += new
    print("Total", total)
    return total


if __name__ == "__main__":
    aoc.run_script(part1)
