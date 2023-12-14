import aoc

import functools
import itertools
import math
import numpy
import re


def roll_row_west(row: str) -> str:
    r = list(row)
    try:
        first_empty = r.index(".")

        for i in range(len(r)):
            if r[i] == ".":
                continue
            elif r[i] == "#":
                first_empty = r.index(".", i)
            else:
                assert r[i] == "O"
                if first_empty > i:
                    continue
                assert first_empty != i, f"{r} {i} {first_empty}"
                r[first_empty] = "O"
                r[i] = "."
                first_empty = r.index(".", first_empty)
    except ValueError:
        pass

    return "".join(r)


def roll_west(grid: list[str]) -> list[str]:
    return [roll_row_west(r) for r in grid]


def roll_north(grid: list[str]) -> list[str]:
    return aoc.transpose(roll_west(aoc.transpose(grid)))


def print_grid(grid: list[str]):
    for row in grid:
        print(row)


def score(grid):
    return sum((len(grid) - i) * row.count("O") for i, row in enumerate(grid))


def part1(input: list[str]) -> int:
    grid = roll_north(input)
    return score(grid)


if __name__ == "__main__":
    result = aoc.run_script(part1)
    print(f"Part 1: {result}")
