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


def karger(edges):
    # print(edges)
    working_edges = edges.copy()
    Vertices = set(v for v, _ in edges)
    Vertices.update(v for _, v in edges)
    merged = {v: {v} for v in Vertices}
    # print("Vertices = ", Vertices)
    while len(Vertices) > 2:
        edge = random.choice(working_edges)
        # print("Remove edge = ", edge)
        # print("Vertices = ", Vertices)
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
    # print("Super nodes A = ", super_node_a)
    # print("Super nodes B = ", super_node_b)
    for edge in edges:
        if (edge[0] in super_node_a and edge[1] in super_node_b) or (
            edge[0] in super_node_b and edge[1] in super_node_a
        ):
            cut_edges.append(edge)
    assert len(cut_edges) == len(
        working_edges
    ), f"{len(cut_edges)} != {len(working_edges)}"

    return cut_edges


def repeat_karger(edges, n=50, target_size=None):
    min_cut = None
    for _ in range(n):
        cut = karger(edges)
        if min_cut is None or len(cut) < len(min_cut):
            min_cut = cut
        if target_size is not None and len(min_cut) <= target_size:
            break
    return min_cut


def part1(data: list[str]) -> int:
    neighbors = collections.defaultdict(set)
    edges = []
    for line in data:
        prefix, suffix = line.split(":")
        for target in suffix.strip().split(" "):
            # Nodes to cut found by inspection
            edges.append((prefix, target))
            neighbors[prefix].add(target)
            neighbors[target].add(prefix)

    while True:
        cut = repeat_karger(edges, target_size=3)
        print("Cut = ", cut)
        if len(cut) == 3:  # Problem statement says there is a cut of size 3
            break

    print("Size = ", len(neighbors))
    for node_a, node_b in cut:
        neighbors[node_a].remove(node_b)
        neighbors[node_b].remove(node_a)

    left_start, right_start = cut[0]
    left = reachable(neighbors, left_start)
    right = reachable(neighbors, right_start)
    assert len(left) + len(right) == len(neighbors)
    return len(left) * len(right)


if __name__ == "__main__":
    result = aoc.run_script(part1, day=25)
    print(f"Part 1: {result}")
