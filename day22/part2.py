#!/usr/bin/env python3
"""Advent of Code 2023 Day 22 Part 2"""

import functools
import itertools
import math
import re
import numpy


import aoc
from day22.part1 import (
    parse,
    find_grid_size,
    make_grid,
    highest_z_beneath,
    X,
    Y,
    Z,
    START,
    END,
)


def place_blocks(blocks):
    max_x, max_y, max_z = find_grid_size(blocks)
    grid = make_grid(max_x, max_y, max_z)
    blocks.sort(key=lambda block: block[0][Z])
    for index, block in enumerate(blocks):
        # print(block, end=' ')
        z_loc = highest_z_beneath(block, grid) + 1
        descent = block[START][Z] - z_loc
        # print("drops by ", descent, end=' => ')
        block[START][Z] -= descent
        block[END][Z] -= descent
        # print(block)
        for x in range(block[START][X], block[END][X] + 1):
            for y in range(block[START][Y], block[END][Y] + 1):
                for z in range(block[START][Z], block[END][Z] + 1):
                    grid[x, y, z] = index + 1

    supports = {}
    for index, block in enumerate(blocks):
        label = index + 1
        supports[label] = set()
        for x in range(block[START][X], block[END][X] + 1):
            for y in range(block[START][Y], block[END][Y] + 1):
                z = block[END][Z] + 1
                if grid[x, y, z] > 0:
                    supports[label].add(grid[x, y, z])

    supported_by = {}
    for index in range(len(blocks)):
        for supported in supports[index + 1]:
            supported_by.setdefault(supported, set()).add(index + 1)

    would_fall = {}
    for index, block in enumerate(blocks):
        label = index + 1
        supported = supports[label]

        would_fall[label] = {label}
        added = True
        while added:
            added = False
            for check, supporters in supported_by.items():
                if check in would_fall[label]:
                    continue  # Already know this falls

                if supporters.issubset(would_fall[label]):
                    would_fall[label].add(check)
                    added = True

    # Subtract one because the block itself doesn't count
    return sum(len(would_fall[label]) - 1 for label in would_fall)


def part1(data: list[str]) -> int:
    blocks = parse(data)
    removable = place_blocks(blocks)

    return removable


if __name__ == "__main__":
    result = aoc.run_script(part1, day=22)
    print(f"Part 1: {result}")
