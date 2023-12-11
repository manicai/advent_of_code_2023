import aoc

import functools
import itertools
import math
import numpy
import re


def find_all(string, substring):
    return [m.start() for m in re.finditer("(?=" + substring + ")", string)]


def expand_universe(input):
    expand_rows = []
    galaxy_cols = set()
    for row in input:
        galaxies = find_all(row, "#")
        if not galaxies:
            expand_rows.append(row)
            expand_rows.append(row)
        else:
            galaxy_cols.update(galaxies)
            expand_rows.append(row)
    all_cols = set(range(len(input[0])))
    empty_cols = all_cols.difference(galaxy_cols)
    # print(empty_cols, len(empty_cols))

    expanded = [
        "".join((".." if i in empty_cols else c) for i, c in enumerate(row))
        for row in expand_rows
    ]
    # print(expanded)
    return expanded


def find_galaxies(universe):
    for r, row in enumerate(universe):
        for c in find_all(row, "#"):
            yield r, c


def pairwise_distances(galaxies):
    for i, (r_start, c_start) in enumerate(galaxies):
        for j in range(i + 1, len(galaxies)):
            (r_end, c_end) = galaxies[j]
            distance = abs(r_end - r_start) + abs(c_end - c_start)
            # print(i + 1, j + 1, distance)
            yield distance


def part1(input: list[str]) -> int:
    universe = expand_universe(input)
    galaxies = list(find_galaxies(universe))
    # print(galaxies)
    return sum(pairwise_distances(galaxies))


if __name__ == "__main__":
    result = aoc.run_script(part1)
    print(f"Part 1: {result}")
