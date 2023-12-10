import aoc

import functools
import itertools
import math
import numpy
import re

# | is a vertical pipe connecting north and south.
# - is a horizontal pipe connecting east and west.
# L is a 90-degree bend connecting north and east.
# J is a 90-degree bend connecting north and west.
# 7 is a 90-degree bend connecting south and west.
# F is a 90-degree bend connecting south and east.
NORTH = (-1, 0)
SOUTH = (1, 0)
EAST = (0, 1)
WEST = (0, -1)
neighbours = {
    "|": [NORTH, SOUTH],
    "-": [EAST, WEST],
    "L": [NORTH, EAST],
    "J": [NORTH, WEST],
    "7": [SOUTH, WEST],
    "F": [SOUTH, EAST],
}

ATTACHED = {NORTH: "|7F", SOUTH: "|LJ", EAST: "-7J", WEST: "-LF"}
DIRECTIONS = list(ATTACHED.keys())


def at(input, position):
    row, column = position
    try:
        return input[row][column]
    except IndexError:
        return "."


def invert(offset):
    r, c = offset
    return -r, -c


def at_offset(input, position, offset):
    r, c = position
    d_r, d_c = offset
    return at(input, (r + d_r, c + d_c))


def move(position, direction):
    p_r, p_c = position
    d_r, d_c = direction
    return p_r + d_r, p_c + d_c


# I could just manually search for this ...
def find_start(input):
    for row, line in enumerate(input):
        if (col := line.find("S")) != -1:
            return row, col


# ... and work this out by hand ...
def infer_start_cell(input, start):
    possible = set(neighbours.keys())
    for offset in ATTACHED:
        neighbour = at_offset(input, start, offset)
        if not neighbour in neighbours:
            assert neighbour in ".S"
            continue
        my_offset = invert(offset)
        if my_offset in neighbours[neighbour]:
            possible = possible.intersection(ATTACHED[my_offset])
    assert len(possible) == 1
    return possible.pop()


def part1(input):
    last_position = find_start(input)
    cell = infer_start_cell(input, last_position)
    # Doesn't matter which way around the grid we go
    position = move(last_position, neighbours[cell][0])
    count = 1
    # Rather than going both ways we are going all the
    # way round then halving the distance.
    while at(input, position) != "S":
        steps = neighbours[at(input, position)]
        cells = [move(position, step) for step in steps]
        assert last_position in cells
        new = [c for c in cells if c != last_position]
        assert len(new) == 1
        last_position = position
        position = new[0]
        count += 1
        # print(at(input, position))

    return count // 2


if __name__ == "__main__":
    result = aoc.run_script(part1)
    print(result)
