#!/usr/bin/env python3
"""Advent of Code 2023 Day 18 Part 1"""

import functools
import itertools
import math
import re
import numpy


import aoc


class Bounds:
    def __init__(self):
        self.east_west = (0, 0)
        self.south_north = (0, 0)

    def update(self, location: tuple[int, int]):
        east_west, south_north = location
        self.east_west = min(self.east_west[0], east_west), max(
            self.east_west[1], east_west
        )
        self.south_north = min(self.south_north[0], south_north), max(
            self.south_north[1], south_north
        )

    def __str__(self) -> str:
        return f"Bounds(east_west={self.east_west}, south_north={self.south_north})"

    def __repr__(self) -> str:
        return str(self)


def parse_line(line: str) -> tuple[str, int]:
    direction, size, _ = line.split()
    size = int(size)
    return direction, size


def find_bounds(data: list[str], parser) -> Bounds:
    location = 0, 0
    bounds = Bounds()
    for step in data:
        direction, size = parser(step)
        if direction == "D":
            location = location[0], location[1] + size
        elif direction == "U":
            location = location[0], location[1] - size
        elif direction == "R":
            location = location[0] + size, location[1]
        elif direction == "L":
            location = location[0] - size, location[1]
        else:
            assert False, f"Unknown direction: {direction}"
        bounds.update(location)

    return bounds


directions = {
    "R": (0, 1),
    "L": (0, -1),
    "D": (1, 0),
    "U": (-1, 0),
}


def move(location: tuple[int, int], direction: str, size: int) -> tuple[int, int]:
    vector = directions[direction]
    return location[0] + size * vector[0], location[1] + size * vector[1]


def print_grid(grid: list[list[str]], location=(None, None)):
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if (i, j) == location:
                print("X", end="")
            else:
                print(cell, end="")
        print()


def trace_route(
    grid: list[list[str]], location: tuple[int, int], route_data: list[str], parser
):
    for step in route_data:
        direction, size = parser(step)
        size = int(size)
        for _ in range(size):
            location = move(location, direction, 1)
            grid[location[0]][location[1]] = "#"
    return grid


def shade_grid(grid: list[list[str]]):
    for row_index, row in enumerate(grid[:-1]):
        in_enclosed_area = False
        for column_index, cell in enumerate(row):
            if cell == "#":
                if grid[row_index + 1][column_index] == "#":
                    in_enclosed_area = not in_enclosed_area
            else:
                if in_enclosed_area:
                    row[column_index] = "#"
    return grid


def part1(data: list[str]) -> int:
    bounds = find_bounds(data, parse_line)
    print(f"Established bounds : {bounds}.", flush=True)
    grid = [
        ["." for _ in range(bounds.east_west[1] - bounds.east_west[0] + 1)]
        for _ in range(bounds.south_north[1] - bounds.south_north[0] + 1)
    ]
    location = abs(bounds.south_north[0]), abs(bounds.east_west[0])
    print("Built grid.", flush=True)
    grid = trace_route(grid, location, data, parse_line)
    # print_grid(grid)
    print("Traced route.", flush=True)
    grid = shade_grid(grid)
    print("Shaded grid.", flush=True)
    return sum(row.count("#") for row in grid)


if __name__ == "__main__":
    result = aoc.run_script(part1, day=18)
    print(f"Part 1: {result}")
