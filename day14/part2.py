import aoc
import aoc.lib

from day14.part1 import roll_north, roll_row_west, roll_west, print_grid, score

import functools
import itertools
import math
import numpy
import re
import hashlib


def roll_row_east(row: str) -> str:
    return roll_row_west(row[::-1])[::-1]


def roll_east(grid: list[str]) -> list[str]:
    return [roll_row_east(r) for r in grid]


def roll_south(grid: list[str]) -> list[str]:
    return aoc.lib.transpose(roll_east(aoc.lib.transpose(grid)))


def cycle(grid: list[str]) -> list[str]:
    n = roll_north(grid)
    w = roll_west(n)
    s = roll_south(w)
    e = roll_east(s)
    return e


def run_cycle(grid: list[str], n: int) -> list[str]:
    hashes = []
    grids = {}
    cycle_point = None
    cycle_count = 0
    for i in range(1000):
        grid = cycle(grid)
        sha = hashlib.sha256("".join(grid).encode("ascii")).hexdigest()
        if sha in hashes:
            break
            # if cycle_point is None:
            #     print(i)
            #     cycle_point = sha
            # elif sha == cycle_point:
            #     print(f"Cycle point: {i}")
            #     cycle_count += 1
            #     if cycle_count == 10:
            #         break

        hashes.append(sha)
        grids[sha] = grid
    print(f"{i} => {hashes.index(sha)}")
    cycle_start = hashes.index(sha)
    cycle_length = i - cycle_start

    cycle_n = (n - cycle_start) % cycle_length
    cycle_sha = hashes[cycle_start + cycle_n - 1]
    return grids[cycle_sha]


def part2(input: list[str]) -> int:
    grid = run_cycle(input, 1000_000_000)
    # print(grid)
    # print_grid(grid)
    return score(grid)


if __name__ == "__main__":
    result = aoc.run_script(part2, day=14)
    print(f"Part 2: {result}")
