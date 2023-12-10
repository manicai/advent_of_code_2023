import aoc
from part1 import *

import functools
import itertools
import math
import numpy
import re


def trace_route(input):
    last_position = find_start(input)
    cell = infer_start_cell(input, last_position)
    # Doesn't matter which way around the grid we go
    position = move(last_position, neighbours[cell][0])
    count = 1
    # Rather than going both ways we are going all the
    # way round then halving the distance.
    route = [last_position]
    while at(input, position) != "S":
        steps = neighbours[at(input, position)]
        cells = [move(position, step) for step in steps]
        assert last_position in cells
        new = [c for c in cells if c != last_position]
        assert len(new) == 1
        last_position = position
        route.append(position)
        position = new[0]
        count += 1
        # print(at(input, position))

    return route


def scrub_map(input, route):
    return [
        "".join(cell if (row, col) in route else "." for col, cell in enumerate(line))
        for row, line in enumerate(input)
    ]


def specify_start(input):
    start = find_start(input)
    cell = infer_start_cell(input, start)
    return [r.replace("S", cell) for r in input]


def print_map(grid):
    for row in grid:
        print(row)


expansions = {
    ".": ["...", "...", "..."],
    "-": ["...", "---", "..."],
    "|": [".|.", ".|.", ".|."],
    "L": [".|.", ".L-", "..."],
    "F": ["...", ".F-", ".|."],
    "J": [".|.", "-J.", "..."],
    "7": ["...", "-7.", ".|."],
}


def expand_map(grid):
    result = []
    for row in grid:
        above = []
        centre = []
        below = []
        for cell in row:
            above.append(expansions[cell][0])
            centre.append(expansions[cell][1])
            below.append(expansions[cell][2])
        result.extend(["".join(above), "".join(centre), "".join(below)])
    return result


def shrink_map(expanded):
    return [
        "".join(c for (j, c) in enumerate(r) if j % 3 == 1)
        for (i, r) in enumerate(expanded)
        if i % 3 == 1
    ]


def paint(grid):
    mutable = [list(row) for row in grid]
    indices = [(0,0),
                (0, len(grid) - 1),
                (len(grid) - 1, 0), 
            (len(grid) - 1, len(grid) - 1)]
    while len(indices) > 0:
        row, col = indices.pop()
        assert mutable[row][col] in ".*"
        if mutable[row][col] == ".":
            mutable[row][col] = "*"
            for d_r, d_c in DIRECTIONS:
                r = row + d_r
                c = col + d_c
                try:
                    if mutable[r][c] == ".":
                        indices.append((r, c))
                except IndexError:
                    pass  # Off the edge
            #print_map(["".join(r) for r in mutable])
            #print()
    return ["".join(r) for r in mutable]


def part2(input):
    route = trace_route(input)
    clean = scrub_map(input, route)
    specific = specify_start(clean)
    expanded = expand_map(specific)
    # print_map(expanded)
    colour = paint(expanded)
    print_map(shrink_map(colour))
    count = sum(r.count(".") for r in shrink_map(colour))
    return count

if __name__ == "__main__":
    result = aoc.run_script(part2)
    print(result)
