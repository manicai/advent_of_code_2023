import aoc
from part1 import LazyMap, LazyMapRange


import functools
import itertools
import math
import re


to_ints = aoc.to_ints


def read_seed_ranges(input):
    for line in input:
        if line.startswith("seeds: "):
            break

    values = to_ints(line[len("seeds: ") :].split())
    assert len(values) % 2 == 0
    return [(values[2 * i], values[2 * i + 1]) for i in range(len(values) // 2)]


def read_maps(input):
    current_map_name = None
    current_map = None
    maps = []
    for line in input:
        if line.endswith("map:"):
            current_map_name = line[:-5]
            current_map = LazyMap()
            continue
        if not line:
            if current_map:
                maps.append((current_map_name, current_map))
            current_map = None
            continue
        if not current_map:
            continue
        assert len(line.split()) == 3, line
        target, source, length = to_ints(line.split())
        lmr = LazyMapRange(source, target, length)
        current_map.add_range(lmr)

    if current_map:
        maps.append((current_map_name, current_map))
    return maps


def find_breakpoints(ranges):
    points = set()
    for r in ranges:
        points.add((r.key_start, r.value_start))
        points.add((r.key_start + r.length, r.value_start + r.length))
    return points


def combine_maps(in_map, out_map):
    breakpoints = find_breakpoints(out_map.ranges)
    result_map = LazyMap()
    for rg in in_map.ranges:
        # print("Range:", rg)
        breaks = set(
            bp
            for bp, _ in breakpoints
            if bp >= rg.value_start and bp < rg.value_start + rg.length
        )
        breaks.update({rg.value_start, rg.value_start + rg.length})
        breaks = sorted(breaks)
        # print("Breakpoints:", breaks)
        for start, end in list(zip(breaks[:-1], breaks[1:])):
            target_offset = start - rg.value_start
            key_start = rg.key_start + target_offset
            length = end - start
            out_value = out_map.value_for(start)
            # print(out_value)
            new = LazyMapRange(key_start, out_value, length)
            # print(new)
            result_map.add_range(new)

    return result_map


def part2(input):
    seed_ranges = read_seed_ranges(input)
    seed_map = LazyMap()
    for s, l in seed_ranges:
        seed_map.add_range(LazyMapRange(s, s, l))
    # print("Seed ranges:", seed_map.ranges)
    maps = read_maps(input)

    for name, lm in maps:
        # print(name, lm.ranges)
        seed_map = combine_maps(seed_map, lm)
        # print(seed_map.ranges)
        # print("84 -> ", seed_map.value_for(84))

    # Minimum location will always be at start of blocks
    min_loc = min(r.value_start for r in seed_map.ranges)
    print("Minimum location:", min_loc)
    return min_loc


def test():
    pass


if __name__ == "__main__":
    pass
    aoc.run_script(part2)
