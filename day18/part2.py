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
    route, length = trace_route((0, 0), data, parse_line)
    print(f"Length: {length}")
    # route.append((0, 0))
    assert route[0] == route[-1], f"Closed loop {route[0]} != {route[-1]}"
    print("Traced route.", flush=True)
    # This will count the main interior area but not account for
    # the fact we're using blocks not points.
    area = shoe_lace(list(reversed(route)))
    # To adjust to blocks add half the length of the perimeter as
    # on average the block is half in half out. Plus one for the
    # starting block.
    area += length / 2 + 1
    assert area == int(area), f"Area {area} is not an integer"
    return int(area)


if __name__ == "__main__":
    result = aoc.run_script(part2, day=18)
    print(f"Part 2: {result}")
