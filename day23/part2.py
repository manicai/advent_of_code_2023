#!/usr/bin/env python3
"""Advent of Code 2023 Day 23 Part 1"""

import collections
import functools
import itertools
import math
import re
import numpy
import sys

sys.setrecursionlimit(10000)


import aoc
from aoc.util import NORTH, SOUTH, EAST, WEST

directions = [NORTH, SOUTH, EAST, WEST]


ICE = {
    ">": EAST,
    "<": WEST,
    "^": NORTH,
    "v": SOUTH,
    "V": SOUTH,
}


def path_to_ice(grid, initial):
    path = [loc for loc in initial]
    while grid[path[-1][0]][path[-1][1]] not in ICE:
        row, col = path[-1]
        candidates = set()
        for d_r, d_c in directions:
            n_r, n_c = row + d_r, col + d_c
            if n_r == len(grid) or n_c == len(grid[0]):
                return path  # Reached edge of map
            if grid[n_r][n_c] == "#":
                continue  # Can't go through the forest
            if (n_r, n_c) in path:
                continue  # Already been here
            candidates.add((n_r, n_c))

        if len(candidates) > 1:
            # It's a node
            return [path[-1]]
        path.append(candidates.pop())
    return path


def find_ice(grid):
    for r, row in enumerate(grid):
        for c, col in enumerate(row):
            if col in ICE:
                yield (r, c), col


Path = collections.namedtuple("Path", ["start", "end", "length"])


def is_adjacent(point, other):
    return abs(point[0] - other[0]) + abs(point[1] - other[1]) == 1


def adjacent_node(point, nodes):
    for node in nodes:
        if is_adjacent(point, node):
            return node
    return None


def dfs(neighbours, start, end):
    def helper(path, cost):
        if path[-1] == end:
            yield path, cost
        else:
            for node, link_cost in neighbours[path[-1]].items():
                if node in path:
                    continue  # Already been here
                for route in helper(path + [node], cost + link_cost):
                    yield route

    for path in helper([start], 0):
        yield path


def part2(grid: list[str]) -> int:
    start = (0, grid[0].index("."))
    end = (len(grid) - 1, grid[-1].index("."))
    print(f"Start: {start}, End: {end}")

    nodes = collections.defaultdict(dict)
    paths = []

    path = path_to_ice(grid, [start, (start[0] + 1, start[1])])
    nodes[start] = {}
    paths.append(Path(start=path[0], end=path[-1], length=len(path)))

    for (r, c), slope in find_ice(grid):
        path = [(r, c), (r + ICE[slope][0], c + ICE[slope][1])]
        path = path_to_ice(grid, path)
        if len(path) == 1:
            nodes[path[0]] = {}
        else:
            paths.append(Path(start=path[0], end=path[-1], length=len(path)))

    for path in paths:
        node_start = adjacent_node(path.start, nodes)
        if node_start is None:
            node_start = start
        node_end = adjacent_node(path.end, nodes)
        if node_end is None:
            node_end = end
        # print(f"{node_start} -> {node_end} is {path.length + 2} long")
        nodes[node_start][node_end] = path.length + 1
        nodes[node_end][node_start] = path.length + 1

    # print(nodes)

    max_cost = -1
    # Could do something smarter but DFS is just about fast enough
    for path, cost in dfs(nodes, start, end):
        # print(cost, path)
        if cost > max_cost:
            max_cost = cost

    return max_cost - 2


# Impatient entry of partial results
# 5891 too low
# 5942 too low
# 6158 too low
if __name__ == "__main__":
    result = aoc.run_script(part2, day=23)
    print(f"Part 2: {result}")
