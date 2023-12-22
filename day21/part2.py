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

623_167_788_247_081 too low
702_322_293_860_496 is maximum I think if you have completely blank grid and
certainly gets rejected as too high.

Max distance on a blank infinite grid is 4 * sum(n for n with same parity as
number of steps).

There are no rocks on the row or column containing the starting position.
Longest string of rocks is 5 (occurs once in a colum and once in a row. There
are 3 instances of 4 in column, 4 instances in a row in my input data).
"""


def calculate(grid, tiles: int) -> int:
    print(f"Calculating for {tiles} tiles")
    e_positions = part1.part1(grid, 140)
    o_positions = part1.part1(grid, 141)

    o_inners = part1.part1(grid, 65)
    o_outers = o_positions - o_inners
    e_inners = part1.part1(grid, 64)
    e_outers = e_positions - e_inners

    print(f"Inner O count {o_inners}")

    number_os = (tiles + 1) ** 2
    number_es = (tiles) ** 2
    print(f"Need {number_os} * {o_positions} (Os) + {number_es} * {e_positions} (Es)")
    count = number_os * o_positions + number_es * e_positions

    boundary_os = tiles + 1
    print(f"Remove {boundary_os} O outers of size {o_outers}")
    count -= boundary_os * o_outers

    boundary_es = tiles
    print(f"Add back {boundary_es} E outers of size {e_outers}")
    count += boundary_es * e_outers

    return count


def part2(grid: list[str]) -> int:
    # noodle(grid)
    steps = 26501365
    tiles = 202300
    # steps = 65
    # tiles = 0
    assert tiles * 131 + 65 == steps
    return calculate(grid, tiles)


if __name__ == "__main__":
    result = aoc.run_script(part2, day=21)
    print(f"Part 2: {result}")
