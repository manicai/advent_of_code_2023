#!/usr/bin/env python3
"""Advent of Code 2023 Day 17 Part 2"""

import functools
import itertools
import math
import re
import numpy


import aoc
from day17.part1 import dijkstra, DIRECTIONS, is_opposite


def at(row, col, grid):
    if row < 0 or row >= len(grid):
        raise IndexError(f"Row {row} out of bounds")
    if col < 0 or col >= len(grid[0]):
        raise IndexError(f"Column {col} out of bounds")
    return grid[row][col]


# Node = (row, column, entry_direction, straight_length, cost)
def find_neighbours(node, grid: list[str]):
    row, column, entry_direction, straight, _ = node
    for exit_direction in DIRECTIONS:
        if straight == 10 and exit_direction == entry_direction:
            continue  # Can't have a straight of length 10
        if is_opposite(exit_direction, entry_direction):
            continue  # Can't reverse direction

        d_row, d_col = exit_direction
        if exit_direction == entry_direction:
            step_size = 1
        else:
            step_size = 4
        try:
            cost = 0
            new_row = row
            new_col = column
            for _ in range(step_size):
                new_row += d_row
                new_col += d_col
                cost += int(at(new_row, new_col, grid))
        except IndexError:
            continue

        new_straight = straight + 1 if exit_direction == entry_direction else 4
        yield (new_row, new_col, exit_direction, new_straight, cost)


def build_map(grid: list[str]):
    start = (0, 0, (0, 0), 0, 0)
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


def dijkstra(graph, start):
    distances = {start: 0}
    pending = {start}
    while len(pending) > 0:
        visiting = pending.pop()
        for neighbour in graph[visiting]:
            _, _, _, _, cost = neighbour
            distance = distances[visiting] + cost
            if neighbour not in distances:
                distances[neighbour] = distance
                pending.add(neighbour)
            elif distance < distances[neighbour]:
                pending.add(neighbour)
                distances[neighbour] = distance

    return distances


def part2(puzzle: list[str]) -> int:
    travel_map = build_map(puzzle)
    distances = dijkstra(travel_map, (0, 0, (0, 0), 0, 0))
    target = (len(puzzle) - 1, len(puzzle[0]) - 1)
    return min(v for (r, c, _, _, _), v in distances.items() if (r, c) == target)


if __name__ == "__main__":
    result = aoc.run_script(part2, day=17)
    print(f"Part 2: {result}")
