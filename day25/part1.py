#!/usr/bin/env python3
"""Advent of Code 2023 Day 25 Part 1"""

import collections
import functools
import itertools
import math
import random
import re
import numpy


import aoc

# Graphviz gave us the following cut
# LEFT = ["xzz", "vkd", "xxq"]
# RIGHT = ["kgl", "qfb", "hqq"]


def karger(edges):
    working_edges = edges.copy()
    Vertices = set(v for v, _ in edges)
    Vertices.update(v for _, v in edges)
    merged = {v: {v} for v in Vertices}
    while len(Vertices) > 2:
        edge = random.choice(working_edges)
        Vertices.remove(edge[1])
        merged[edge[0]].update(merged[edge[1]])
        del merged[edge[1]]
        for i, e in enumerate(working_edges):
            if e[1] == edge[1]:
                working_edges[i] = (e[0], edge[0])
            elif e[0] == edge[1]:
                working_edges[i] = (edge[0], e[1])
        working_edges = [(a, b) for a, b in working_edges if a != b]

    cut_edges = []
    super_node_a, super_node_b = merged.values()
    for edge in edges:
        if (edge[0] in super_node_a and edge[1] in super_node_b) or (
            edge[0] in super_node_b and edge[1] in super_node_a
        ):
            cut_edges.append(edge)
    assert len(cut_edges) == len(
        working_edges
    ), f"{len(cut_edges)} != {len(working_edges)}"

    return cut_edges, [super_node_a, super_node_b]


def repeat_karger(edges, n=50, target_size=None):
    min_cut = None
    min_cut_partition = None
    for _ in range(n):
        cut, partition = karger(edges)
        if min_cut is None or len(cut) < len(min_cut):
            min_cut = cut
            min_cut_partition = partition
        if target_size is not None and len(min_cut) <= target_size:
            break
    return min_cut, min_cut_partition


def part1(data: list[str]) -> int:
    edges = []
    for line in data:
        prefix, suffix = line.split(":")
        for target in suffix.strip().split(" "):
            # Nodes to cut found by inspection
            edges.append((prefix, target))

    known_size = 3  # Problem statement says there is a cut of size 3
    while True:
        cut, partition = repeat_karger(edges, target_size=known_size)
        print("Cut", cut, "too large" if len(cut) > known_size else "found")
        if len(cut) == known_size:
            break

    return math.prod(len(p) for p in partition)


if __name__ == "__main__":
    result = aoc.run_script(part1, day=25)
    print(f"Part 1: {result}")
