#!/usr/bin/env python3
"""Advent of Code 2023 Day 23 Part 1"""

import functools
import itertools
import math
import re
import numpy
import sys

sys.setrecursionlimit(10000)


import aoc
from aoc.util import NORTH, SOUTH, EAST, WEST

directions = [NORTH, SOUTH, EAST, WEST]


ICE = {
    ">": EAST,
    "<": WEST,
    "^": NORTH,
    "v": SOUTH,
    "V": SOUTH,
}


def dfs(grid, start, end):
    def helper(path):
        if path[-1] == end:
            yield path
        else:
            row, col = path[-1]
            for d_r, d_c in directions:
                n_r, n_c = row + d_r, col + d_c
                if grid[n_r][n_c] == "#":
                    continue  # Can't go through the forest
                if (n_r, n_c) in path:
                    continue  # Already been here
                if grid[n_r][n_c] in ICE and ICE[grid[n_r][n_c]] != (d_r, d_c):
                    continue  # Can't go against the ice
                for route in helper(path + [(n_r, n_c)]):
                    yield route

    # Hard code for ease as it means we don't have to worry about the edge
    # of the map from now on.
    first_step = (start[0] + 1, start[1])
    for path in helper([start, first_step]):
        yield path


def part1(grid: list[str]) -> int:
    start = (0, grid[0].index("."))
    end = (len(grid) - 1, grid[-1].index("."))
    print(f"Start: {start}, End: {end}")
    max_len = -1
    for path in dfs(grid, start, end):
        step_list = list(path)
        print(len(step_list))
        if (length := len(step_list)) > max_len:
            max_len = length

    # Subtract 1 as we count steps not squares
    return max_len - 1


if __name__ == "__main__":
    result = aoc.run_script(part1, day=23)
    print(f"Part 1: {result}")
