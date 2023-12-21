#!/usr/bin/env python3
"""Advent of Code 2023 Day 21 Part 2"""

import functools
import itertools
import math
import re
import numpy


import aoc
import aoc.util
import day21.part1 as part1

NOTES = """
Grid size of main puzzle is 131 x 131
Number of steps the elf wants to walk is 26501365 which is 202300 * 131 + 65.

623_950_055_605_800
623_167_788_247_081 too low
702_322_293_860_496 is maximum I think if you have completely blank grid and
certainly gets rejected as too high.

Max distance on a blank infinite grid is 4 * sum(n for n with same parity as
number of steps).

There are no rocks on the row or column containing the starting position.
Longest string of rocks is 5 (occurs once in a colum and once in a row. There
are 3 instances of 4 in column, 4 instances in a row in my input data).
"""
# STEPS = 26501365
STEPS = 65

#  +-----+-----+
#  | ULO/|\URO |
#  |   / | \   |
#  |  /  |  \  |
#  | /ULI|URI\ |
#  |/    |    \|
#  +-----------|
#  |\    |    /|
#  | \LLI|LRI/ |
#  |  \  |  /  |
#  |   \ | /   |
#  | LLO\|/LRO |
#  +-----+-----+
segments = {
    "ULO": (lambda r, c: (r < 65 and c < 65 and r + c < 65), "a"),
    # "ULI": (lambda r, c: (r < 65 and c < 65 and r + c >= 65), 'b'),
    # "URI": (lambda r, c: (r < 65 and c > 65 and c - 66 < r), 'c'),
    "URO": (lambda r, c: (r < 65 and c > 65 and c - 66 >= r), "d"),
    # "LLI": (lambda r, c: (r > 65 and c < 65 and r - 66 < c), 'e'),
    "LLO": (lambda r, c: (r > 65 and c < 65 and r - 66 >= c), "f"),
    # "LRI": (lambda r, c: (r > 65 and c > 65 and r + c < 196), 'g'),
    "LRO": (lambda r, c: (r > 65 and c > 65 and r + c >= 196), "h"),
}


def print_marked_grid(grid, locations):
    for r, row in enumerate(grid):
        for c, char in enumerate(row):
            if (r, c) in locations:
                print("O" if char == "." else "o", end="")
            else:
                print(char, end="")
        print()


def calculate_grid_position_counts(grid: list[str]) -> dict[int, dict[str, int]]:
    counts = {}
    for parity in [0, 1]:
        spaces_counts = {key: 0 for key in segments}
        for r, row in enumerate(grid):
            for c, col in enumerate(row):
                if col == "." and (r + c) % 2 == parity:
                    for key, (selector, _) in segments.items():
                        if selector(r, c):
                            spaces_counts[key] += 1
        counts[parity] = spaces_counts
    return counts


def part2(grid: list[str]) -> int:
    print(f"Grid size is {len(grid)}x{len(grid[0])}")

    r_s, c_s = part1.find_start(grid)
    print(f"Start is at ({r_s}, {c_s})")
    locations = part1.find_locations(grid, STEPS)

    blank = [
        "".join("S" if (r == r_s and c == c_s) else "." for c in range(len(grid[0])))
        for r in range(len(grid))
    ]
    blank_locations = part1.find_locations(blank, STEPS)
    print(f"Locations: {len(locations)}, blank locations: {len(blank_locations)}")

    lgrid = [list(row) for row in grid]
    for i, key in enumerate(segments):
        for r, row in enumerate(grid):
            for c, col in enumerate(row):
                selector, label = segments[key]
                if selector(r, c) and col == ".":
                    lgrid[r][c] = label

    print_marked_grid(["".join(c) for c in lgrid], locations)
    # Sanity checks
    max_distance = 0
    for r, c in locations:
        distance = abs(r - r_s) + abs(c - c_s)
        if distance > max_distance:
            max_distance = distance
    print(f"Max distance is {max_distance}")
    for r, c in locations:
        assert (r + c) % 2 == (STEPS % 2), f"({r}, {c}) is wrong parity"

    # Count rocks in each segment of tile
    spaces_counts = {key: 0 for key in segments}
    for r, row in enumerate(grid):
        for c, col in enumerate(row):
            if col == "." and (r + c) % 2 == (STEPS % 2):
                for key, (selector, _) in segments.items():
                    if selector(r, c):
                        spaces_counts[key] += 1
    print(spaces_counts)

    print(calculate_grid_position_counts(grid))
    return max_distance


if __name__ == "__main__":
    result = aoc.run_script(part2, day=21)
    print(f"Part 2: {result}")
