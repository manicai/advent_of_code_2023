#!/usr/bin/env python3
"""Advent of Code 2023 Day 18 Part 2"""

import functools
import itertools
import math
import re
import numpy


import aoc
import day18.part1 as part1


DIRECTIONS = "LDRU"


def parse_line(line: str) -> tuple[str, int]:
    _, _, hex_code = line.split()
    hex_code = hex_code[1:-1]  # Strip off the braces
    direction = int(hex_code[-1])
    assert hex_code[0] == "#"
    size = int(hex_code[1:-1], 16)
    return DIRECTIONS[direction], size


def trace_route(location, route_data: list[str], parser):
    locations = [location]
    length = 0
    for stage in route_data:
        direction, step_size = parser(stage)
        length += step_size
        vector = part1.directions[direction]
        location = (
            location[0] + step_size * vector[0],
            location[1] + step_size * vector[1],
        )
        locations.append(location)
    return locations, length


def shoe_lace(locations):
    area = 0
    for point, next in zip(locations, locations[1:]):
        p_x, p_y = point
        n_x, n_y = next
        delta = p_x * n_y - p_y * n_x
        # print(f"({p_x}, {p_y}) -> ({n_x}, {n_y}) -> {delta}")
        area += delta
    return abs(area) / 2


def part2(data: list[str]) -> int:
    # The (0.5, 0.5) is an arbitrary offset that puts the line of the route
    # in the middle of all the blocks it passes through. We don't need this
    # but it makes it easier to think about what's going on.
    route, length = trace_route((0.5, 0.5), data, parse_line)
    assert route[0] == route[-1], f"Closed loop {route[0]} != {route[-1]}"
    print("Traced route.", flush=True)
    # Calculate the area inside the route. The route line is going down
    # the middle of the blocks so we are leaving off the parts of the block
    # outside.
    area = shoe_lace(list(reversed(route)))
    # Now we need to add the area of the blocks that are outside the route
    # i.e. all the ones on the perimeter. If going clockwise for right turns
    # we will so far only have counted a quarter of the turn block but for
    # left turns we will have counted three quarters. Straights are a half,
    # fairly obviously. Since it is a closed loop the of right and left turns
    # cancels out so we can just add half the length. Then need to add one
    # more for the starting block.
    area += length / 2 + 1
    assert area == int(area), f"Area {area} is not an integer"
    return int(area)


if __name__ == "__main__":
    result = aoc.run_script(part2, day=18)
    print(f"Part 2: {result}")
