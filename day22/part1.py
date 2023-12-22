#!/usr/bin/env python3
"""Advent of Code 2023 Day 22 Part 1"""

import functools
import itertools
import math
import re
import numpy


import aoc

X = 0
Y = 1
Z = 2
START = 0
END = 1


def parse(data: list[str]) -> list[tuple[list[int], list[int]]]:
    blocks = []
    for line in data:
        start, end = line.split("~")
        start = list(int(n) for n in start.split(","))
        end = list(int(n) for n in end.split(","))
        blocks.append((start, end))
    return blocks


def find_grid_size(blocks):
    max_x, max_y, max_z = 0, 0, 0
    for block in blocks:
        assert block[START][X] <= block[END][X]
        assert block[START][Y] <= block[END][Y]
        assert block[START][Z] <= block[END][Z]
        x, y, z = block[1]
        if x > max_x:
            max_x = x
        if y > max_y:
            max_y = y
        if z > max_z:
            max_z = z
    return max_x, max_y, max_z


def make_grid(max_x, max_y, max_z):
    grid = numpy.zeros((max_x + 1, max_y + 1, max_z + 2), dtype=numpy.int16)
    for x in range(max_x + 1):
        for y in range(max_y + 1):
            grid[x, y, 0] = 10_000
    return grid


def highest_z_beneath(block, grid):
    start, end = block
    for z in range(block[0][Z] - 1, -1, -1):
        for x in range(start[X], end[X] + 1):
            for y in range(start[Y], end[Y] + 1):
                if grid[x, y, z] > 0:
                    return z
    assert False, "Bottom layer should be all 1s"


def place_blocks(blocks):
    max_x, max_y, max_z = find_grid_size(blocks)
    grid = make_grid(max_x, max_y, max_z)
    blocks.sort(key=lambda block: block[0][Z])
    for index, block in enumerate(blocks):
        print(block, end=" ")
        z_loc = highest_z_beneath(block, grid) + 1
        descent = block[START][Z] - z_loc
        print("drops by ", descent, end=" => ")
        block[START][Z] -= descent
        block[END][Z] -= descent
        print(block)
        for x in range(block[START][X], block[END][X] + 1):
            for y in range(block[START][Y], block[END][Y] + 1):
                for z in range(block[START][Z], block[END][Z] + 1):
                    grid[x, y, z] = index + 1

    supports = {}
    for index, block in enumerate(blocks):
        supports[index + 1] = set()
        for x in range(block[START][X], block[END][X] + 1):
            for y in range(block[START][Y], block[END][Y] + 1):
                z = block[END][Z] + 1
                if grid[x, y, z] > 0:
                    supports[index + 1].add(grid[x, y, z])

    supported_by = {}
    for index in range(len(blocks)):
        for supported in supports[index + 1]:
            supported_by.setdefault(supported, set()).add(index + 1)

    removable = []
    for index, block in enumerate(blocks):
        label = index + 1
        supported = supports[label]
        print(
            f"{label}: (f{block}) supports {supported} and is supported by {supported_by.get(label, set())}",
            end=" ",
        )
        can_remove = True
        for supported_block in supported:
            if len(supported_by[supported_block]) == 1:
                can_remove = False
        print("can remove" if can_remove else "cannot remove")
        if can_remove:
            removable.append(label)

    return len(removable)


def part1(data: list[str]) -> int:
    blocks = parse(data)
    removable = place_blocks(blocks)

    return removable


if __name__ == "__main__":
    result = aoc.run_script(part1, day=22)
    print(f"Part 1: {result}")
