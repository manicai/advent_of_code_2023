import aoc
import part1

import functools
import itertools
import math
import numpy
import re


def part2(input):
    graph = part1.read_graph(input)
    steps = input[0]

    locations = dict((k, k) for k in graph if k[-1] == "A")
    # print(locations)
    counts = {}
    for location in locations:
        count = 0
        current = location
        while current[-1] != "Z":
            direction = steps[count % len(steps)]
            current = graph[current][direction]
            # print(count, locations)
            count += 1
        counts[location] = count
    print(counts)
    print(numpy.lcm.reduce(list(counts.values())))


if __name__ == "__main__":
    aoc.run_script(part2)
