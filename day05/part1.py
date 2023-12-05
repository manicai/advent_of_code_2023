import aoc

import functools
import itertools
import math
import re


class LazyMapRange:
    def __init__(self, key_start, value_start, length):
        self.key_start = key_start
        self.value_start = value_start
        self.length = length

    def contains(self, key):
        return key >= self.key_start and key < (self.key_start + self.length)

    def value_for(self, key):
        assert self.contains(key)
        offset = key - self.key_start
        return self.value_start + offset

    def __str__(self):
        return f"[{self.key_start} -> {self.key_start  + self.length - 1}] => {self.value_start}"


class LazyMap:
    def __init__(self):
        self.ranges = []

    def add_range(self, lr):
        self.ranges.append(lr)

    def _find_range(self, key):
        matching = [r for r in self.ranges if r.contains(key)]
        assert len(matching) < 2
        return matching[0] if matching else None

    def contains(self, key):
        return self._find_range(key) is not None

    def value_for(self, key):
        r = self._find_range(key)
        if r:
            return r.value_for(key)
        else:
            return key

    def __str__(self):
        return "{ " + ", ".join(str(r) for r in self.ranges) + " }"

    def __repr__(self):
        return self.__str__()


map_names = [
    "seed-to-soil",
    "soil-to-fertilizer",
    "fertilizer-to-water",
    "water-to-light",
    "light-to-temperature",
    "temperature-to-humidity",
    "humidity-to-location",
]


def read_seeds(input):
    for line in input:
        if not line.startswith("seeds:"):
            continue
        trimmed = line[len("seeds:") :]
        return [int(seed) for seed in trimmed.split()]


def read_map(name, input):
    read_line = False
    lm = LazyMap()
    for line in input:
        if line.startswith(name):
            read_line = True
            continue
        if not read_line:
            continue
        if not line:  # Stop reading at next blank line.
            return lm
        target, source, length = (int(n) for n in line.split())
        lmr = LazyMapRange(source, target, length)
        lm.add_range(lmr)
    # If we've run out of input return what we go.
    return lm


def trace_maps(seed, maps):
    steps = [seed]
    for name in map_names:
        # print(name, steps)
        steps.append(maps[name].value_for(steps[-1]))
    return steps


def part1(input):
    print(input)
    seeds = read_seeds(input)
    print("Seeds:", seeds)
    maps = dict((m, read_map(m, input)) for m in map_names)
    # for k, v in maps.items():
    #     print(k, " :: ", v)

    locations = []
    for seed in seeds:
        steps = trace_maps(seed, maps)
        # print(steps)
        locations.append(steps[-1])

    print("Nearest location:", min(locations))


# Seed 79, soil 81, fertilizer 81, water 81, light 74, temperature 78, humidity 78, location 82.
# Seed 14, soil 14, fertilizer 53, water 49, light 42, temperature 42, humidity 43, location 43.
# Seed 55, soil 57, fertilizer 57, water 53, light 46, temperature 82, humidity 82, location 86.
# Seed 13, soil 13, fertilizer 52, water 41, light 34, temperature 34, humidity 35, location 35.


def test():
    lmr = LazyMapRange(10, 20, 5)
    assert not lmr.contains(9)
    assert lmr.contains(10)
    assert lmr.contains(14)
    assert not lmr.contains(15)
    assert lmr.value_for(10) == 20
    assert lmr.value_for(14) == 24
    assert str(lmr) == "[10 -> 14] => 20", str(lmr)

    lm = LazyMap()
    lm.add_range(lmr)
    lm.add_range(LazyMapRange(100, 200, 100))
    assert not lm.contains(9)
    assert lm.contains(10)
    assert lm.contains(14)
    assert not lm.contains(15)
    assert lm.value_for(10) == 20
    assert lm.value_for(14) == 24
    assert not lm.contains(99)
    assert lm.contains(199)
    assert lm.value_for(199) == 299
    assert lm.value_for(150) == 250


if __name__ == "__main__":
    test()
    aoc.run_script(part1)
