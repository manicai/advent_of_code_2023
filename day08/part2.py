import aoc
import part1

import functools
import itertools
import math
import re


def finished(locations):
    for current in locations.values():
        if current[-1] != "Z":
            return False
    return True


def find_factors(number):
    for n in range(2, number):
        if number % n == 0:
            return [n] + find_factors(number // n)
    return [number]


def lowest_common_multiple(numbers):
    print(numbers)
    factors = [find_factors(n) for n in numbers]
    print(factors)
    union = set(n for s in factors for n in s)
    lcm = 1
    for n in union:
        count = max(s.count(n) for s in factors)
        assert count >= 1
        lcm *= n**count
    return lcm


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
    print(lowest_common_multiple(counts.values()))


if __name__ == "__main__":
    aoc.run_script(part2)
