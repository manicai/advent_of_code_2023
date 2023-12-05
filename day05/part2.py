import aoc
import part1


import functools
import itertools
import math
import re


def part2(input):
    seeds = part1.read_seeds(input)
    maps = dict((m, part1.read_map(m, input)) for m in part1.map_names)
    # print(seeds)
    ranges = [(seeds[i - 1], n) for i, n in enumerate(seeds) if i % 2 == 1]
    best_locations = []
    for start, length in ranges:
        best = None
        for seed in range(start, start + length):
            steps = part1.trace_maps(seed, maps)
            location = steps[-1]
            if best is None or best > location:
                best = location
                print(best)
        print((start, length), " -> ", best)
        best_locations.append(best)

    print("Best location =", min(best_locations))


if __name__ == "__main__":
    aoc.run_script(part2)
