import aoc
import part1

import functools
import itertools
import math
import numpy
import re

def back_extrapolate(seq) -> int:
    # print(seq)
    if not any(seq):
        return 0
    delta = back_extrapolate(list(x-y for x,y in itertools.pairwise(seq)))
    # print(delta)
    return seq[0] + delta


def part2(input):
    total = 0
    for line in input:
        values = aoc.to_ints(line.split())
        new = back_extrapolate(values)
        print(f"{line} -> {new}")
        total += new
    print("Total", total)
    return total


if __name__ == "__main__":
    aoc.run_script(part2)
