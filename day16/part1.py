#!/usr/bin/env python3
"""Advent of Code 2023 Day 16 Part 1"""

from collections import defaultdict
import functools
import itertools
import math
import re
import numpy


import aoc

NORTH = (-1, 0)
SOUTH = (1, 0)
EAST = (0, 1)
WEST = (0, -1)

# cell -> direction -> list of new directions
steps = {
    ".": {
        EAST: [EAST],
        WEST: [WEST],
        SOUTH: [SOUTH],
        NORTH: [NORTH],
    },
    "|": {
        EAST: [NORTH, SOUTH],
        WEST: [NORTH, SOUTH],
        SOUTH: [SOUTH],
        NORTH: [NORTH],
    },
    "-": {
        SOUTH: [EAST, WEST],
        NORTH: [EAST, WEST],
        EAST: [EAST],
        WEST: [WEST],
    },
    "/": {
        EAST: [NORTH],
        SOUTH: [WEST],
        WEST: [SOUTH],
        NORTH: [EAST],
    },
    "\\": {
        EAST: [SOUTH],
        SOUTH: [EAST],
        WEST: [NORTH],
        NORTH: [WEST],
    },
}


def trace_route(grid: list[str], current) -> set[tuple[int, int]]:
    # Pending is a list of cells and the directions we are leaving them in.
    pending = [current]
    # Visited is a set of cells we have visited and directions we left in.
    visited = set([current])
    # print("Starting at", visited)
    while pending:
        row, col, (d_r, d_c) = pending.pop()
        # print(row, col, (d_r, d_c))
        new_row, new_col = row + d_r, col + d_c
        if (
            new_row < 0
            or new_col < 0
            or new_row >= len(grid)
            or new_col >= len(grid[0])
        ):
            continue  # Outside the grid

        cell = grid[new_row][new_col]
        for new_direction in steps[cell][(d_r, d_c)]:
            next = (new_row, new_col, new_direction)
            if next not in visited:
                # print("Adding", next)
                pending.append(next)
                visited.add(next)

    # Only interested in visited cells
    # print(visited)
    return {(r, c) for r, c, _ in visited}


def part1(input: list[str]) -> int:
    for r in input:
        print(r)
    print()
    visited = trace_route(input, (0, 0, EAST))
    for i_r, r in enumerate(input):
        for i_c, c in enumerate(r):
            if (i_r, i_c) in visited:
                print("#", end="")
            else:
                print(c, end="")
        print()
    return len(visited)


if __name__ == "__main__":
    result = aoc.run_script(part1, day=16)
    print(f"Part 1: {result}")
