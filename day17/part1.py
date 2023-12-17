#!/usr/bin/env python3
"""Advent of Code 2023 Day 17 Part 1"""

import functools
import itertools
import math
import re
import numpy


import aoc


NORTH = (-1, 0)
SOUTH = (1, 0)
EAST = (0, 1)
WEST = (0, -1)
DIRECTIONS = [NORTH, SOUTH, EAST, WEST]


# Node = (row, column, entry_direction, straight_length)
def find_neighbours(node, grid):
    row, column, entry_direction, straight = node
    for exit_direction in DIRECTIONS:
        if straight == 3 and exit_direction == entry_direction:
            continue  # Can't have a straight of length 4
        d_row, d_col = exit_direction
        new_row = row + d_row
        new_col = column + d_col
        if new_row < 0 or new_row >= len(grid):
            continue  # Out of bounds
        if new_col < 0 or new_col >= len(grid[0]):
            continue
        new_straight = straight + 1 if exit_direction == entry_direction else 1

        yield (new_row, new_col, exit_direction, new_straight)


def build_map(grid: list[str]):
    start = (0, 0, (0, 0), 0)
    pending = {start}
    visited = {}
    while len(pending) > 0:
        visiting = pending.pop()
        if visiting in visited:
            continue
        neighbours = list(find_neighbours(visiting, grid))
        visited[visiting] = neighbours
        for neighbour in neighbours:
            if neighbour not in visited:
                pending.add(neighbour)

    return visited


def dijkstra(graph, costs, start):
    distances = {start: 0}
    pending = {start}
    while len(pending) > 0:
        visiting = pending.pop()
        for neighbour in graph[visiting]:
            r, c, _, _ = neighbour
            cost = costs[r][c]
            distance = distances[visiting] + cost
            if neighbour not in distances:
                distances[neighbour] = distance
                pending.add(neighbour)
            elif distance < distances[neighbour]:
                pending.add(neighbour)
                distances[neighbour] = distance

    return distances


def part1(puzzle: list[str]) -> int:
    costs = [[int(c) for c in row] for row in puzzle]
    m = build_map(puzzle)
    print(len(puzzle), len(puzzle[0]), "->", len(puzzle) * len(puzzle[0]))
    print(len(m))
    print(m[(4, 5, (1, 0), 3)])
    print(costs[4][5])
    target = len(puzzle) - 1, len(puzzle[0]) - 1
    distances = dijkstra(m, costs, (0, 0, (0, 0), 0))
    for k, v in distances.items():
        r, c, _, _ = k
        if (r, c) == target:
            print(k, v)


if __name__ == "__main__":
    result = aoc.run_script(part1, day=17)
    print(f"Part 1: {result}")
