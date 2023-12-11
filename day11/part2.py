import aoc
from part1 import find_all, find_galaxies

import functools
import itertools
import math
import numpy
import re


def super_expand_universe(input):
    expand_rows = []
    galaxy_cols = set()
    for row in input:
        galaxies = find_all(row, "#")
        if not galaxies:
            expand_rows.append('+' * len(row))
        else:
            galaxy_cols.update(galaxies)
            expand_rows.append(row)
    all_cols = set(range(len(input[0])))
    empty_cols = all_cols.difference(galaxy_cols)

    expanded = [
        "".join(("+" if i in empty_cols else c) for i, c in enumerate(row))
        for row in expand_rows
    ]
    return expanded


def measure_distance(start, end, universe, expansion):
    r_start = min(start[0], end[0])
    r_end = max(start[0], end[0])
    c_start = min(start[1], end[1])
    c_end = max(start[1], end[1])

    # print(start, end)
    row_count = 0
    for r in range(r_start + 1, r_end + 1):
        if universe[r][c_start] == "+":
            row_count += expansion
        else:
            row_count += 1
    col_count = 0
    for c in range(c_start + 1, c_end + 1):
        # print(universe[r_end][c], end=" : ")
        if universe[r_end][c] == "+":
            col_count += expansion
        else:
            col_count += 1
    # print(row_count, col_count)
    return row_count + col_count


def pairwise_distances(galaxies, universe, expansion=1_000_000):
    for i, start in enumerate(galaxies):
        for j in range(i + 1, len(galaxies)):
            end = galaxies[j]
            # print(i + 1, j + 1)
            distance = measure_distance(start, end, universe, expansion)
            # print(distance)
            # print()
            yield distance


def print_universe(universe):
    for row in universe:
        print(row)


def print_counted_universe(universe):
    count = 1
    for row in universe:
        for c in row:
            if c == "#":
                print(count, end="")
                count += 1
            else:
                print(c, end="")
        print()


def part2(input: list[str]) -> int:
    universe = super_expand_universe(input)
    # print_counted_universe(universe)
    galaxies = list(find_galaxies(universe))
    # print(galaxies)
    return sum(pairwise_distances(galaxies, universe))


if __name__ == "__main__":
    result = aoc.run_script(part2)
    print(f"Part 2: {result}")
