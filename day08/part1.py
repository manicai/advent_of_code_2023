import aoc

import functools
import itertools
import math
import re


PATTERN = r"([0-9A-Z]+) = \(([0-9A-Z]+), ([0-9A-Z]+)\)"


def read_graph(input):
    graph = {}
    for line in input:
        if not "=" in line:
            continue

        match = re.match(PATTERN, line)
        assert match, line
        src = match.group(1)
        dest = {"L": match.group(2), "R": match.group(3)}
        graph[src] = dest
    return graph


def part1(input):
    steps = input[0]
    location = "AAA"
    count = 0
    offset = 0
    graph = read_graph(input)
    while location != "ZZZ":
        direction = steps[offset]
        location = graph[location][direction]
        offset = (offset + 1) % len(steps)
        count += 1
        print(count, location)
    print(count)


if __name__ == "__main__":
    aoc.run_script(part1)
