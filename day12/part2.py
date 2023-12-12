import aoc
from part1 import *

import functools
import itertools
import math
import numpy
import re


def part2(input: list[str]) -> int:
    total = 0
    for line in input:
        coils, pattern = parse_line(line)
        coils = ((coils + "?") * 5)[:-1]
        pattern = pattern * 5
        count = count_possible_matches(coils, pattern)
        print(f"{coils} {pattern} {count}")
        total += count
    return total


if __name__ == "__main__":
    result = aoc.run_script(part2)
    print(f"Part 2: {result}")
