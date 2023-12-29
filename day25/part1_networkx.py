#!/usr/bin/env python3
"""Advent of Code 2023 Day 25 Part 1"""

import math
import networkx as nx

import aoc


def part1(data: list[str]) -> int:
    G = nx.Graph()
    for line in data:
        prefix, suffix = line.split(":")
        for target in suffix.strip().split(" "):
            G.add_edge(prefix, target, weight=1)

    cut_value, partition = nx.stoer_wagner(G)
    assert cut_value == 3
    return math.prod([len(x) for x in partition])


if __name__ == "__main__":
    result = aoc.run_script(part1, day=25)
    print(f"Part 1: {result}")
