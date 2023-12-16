#!/usr/bin/env python3
"""Advent of Code 2023 Day 16 Part 2"""

import functools
import itertools
import math
import re
import numpy


import aoc
from day16.part1 import trace_route, NORTH, SOUTH, EAST, WEST


def part2(input: list[str]) -> int:
    row_length = len(input[0])
    candidates = (
        [(r, 0, EAST) for r in range(len(input))]
        + [(r, row_length - 1, WEST) for r in range(len(input))]
        + [(0, c, SOUTH) for c in range(row_length)]
        + [(len(input) - 1, c, NORTH) for c in range(row_length)]
    )
    max_count = -1
    # We could remove candidates we've hit on other journeys as we
    # go, but it's not worth the effort.
    for r, c, d in candidates:
        # print("Trying", r, c, d)
        count = len(trace_route(input, (r, c, d)))
        if count > max_count:
            max_count = count
    return max_count


if __name__ == "__main__":
    result = aoc.run_script(part2, day=16)
    print(f"Part 2: {result}")
