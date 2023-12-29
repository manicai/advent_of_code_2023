#!/usr/bin/env python3
"""Advent of Code 2023 Day 25 Part 1"""

import collections
import functools
import itertools
import math
import re
import numpy


import aoc

LEFT = ["xzz", "vkd", "xxq"]
RIGHT = ["kgl", "qfb", "hqq"]


def convert_to_graphwiz(data):
    for line in data:
        prefix, suffix = line.split(":")
        for target in suffix.strip().split(" "):
            print(f"{prefix} -> {target}")


def reachable(neighbors, start):
    visited = set()
    queue = [start]
    while queue:
        node = queue.pop()
        if node in visited:
            continue
        visited.add(node)
        queue.extend(neighbors[node])
    return visited


def part1(data: list[str]) -> int:
    neighbors = collections.defaultdict(set)
    for line in data:
        prefix, suffix = line.split(":")
        for target in suffix.strip().split(" "):
            # Nodes to cut found by inspection
            if prefix in LEFT and target in RIGHT:
                print(f"{prefix} -> {target}")
                continue
            neighbors[prefix].add(target)
            neighbors[target].add(prefix)

    print("Size = ", len(neighbors))

    left = reachable(neighbors, LEFT[0])
    right = reachable(neighbors, RIGHT[0])
    assert len(left) + len(right) == len(neighbors)

    return len(left) * len(right)


if __name__ == "__main__":
    result = aoc.run_script(part1, day=25)
    print(f"Part 1: {result}")
