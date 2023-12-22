#!/usr/bin/env python3
"""Advent of Code 2023 Day 21 Part 1"""

import functools
import itertools
import math
import re
import numpy


import aoc


def find_neighbours(grid: list[str], row: int, col: int) -> set[(int, int)]:
    def valid(r, c):
        if r < 0 or c < 0:
            return False
        elif r >= len(grid) or c >= len(grid[r]):
            return False
        elif grid[r][c] == "#":
            return False
        return True

    neighbours = set()
    for r in [row - 1, row + 1]:
        if valid(r, col):
            neighbours.add((r, col))
    for c in [col - 1, col + 1]:
        if valid(row, c):
            neighbours.add((row, c))
    return neighbours


def find_start(data: list[str]) -> (int, int):
    for r, row in enumerate(data):
        if (c := row.find("S")) != -1:
            return (r, c)


def find_locations(grid, iterations):
    locations = {find_start(grid)}
    for _ in range(iterations):
        new_locations = set()
        for location in locations:
            new_locations |= find_neighbours(grid, *location)
        locations = new_locations

    return locations


def print_marked_grid(grid, locations):
    for r, row in enumerate(grid):
        for c, char in enumerate(row):
            if (r, c) in locations:
                print("O", end="")
            else:
                print(char, end="")
        print()


def part1(data: list[str], steps=65) -> int:
    locations = find_locations(data, steps)
    return len(locations)


if __name__ == "__main__":
    result = aoc.run_script(part1, day=21)
    print(f"Part 1: {result}")
