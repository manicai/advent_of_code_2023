import aoc

try:
    from .part1 import *
except ImportError:
    from part1 import *

import functools
import itertools
import math
import numpy
import re
import time


def get_cache(line) -> int:
    with open("cache.txt", "r") as f:
        for l in f:
            if l.startswith(line + "::"):
                return int(l.split("::")[1])
    return None


def cache(line, count):
    with open("cache.txt", "a") as f:
        f.write(f"{line}::{count}\n")


def cached(func):
    def wrapper(line):
        if (result := get_cache(line)) is None:
            result = func(line)
            cache(line, result)
        return result

    return wrapper


# Highest block seen in data was 16
res = {i: re.compile(f"(?=([#?]{{{i}}}([?.]|$)))") for i in range(1, 20)}


def count_matches(coils: str, pattern: str, depth=0) -> int:
    def log(*args):
        # print('   ' * depth, *args, flush=True)
        pass

    log(f"Looking for {pattern} in '{coils}'")

    if not pattern:
        return 1 if "#" not in coils else 0

    if pattern == [1]:
        hashes = coils.count("#")
        if hashes == 1:
            return 1
        elif hashes > 1:
            return 0
        return coils.count("?")

    block = max(pattern)
    index = pattern.index(block)
    count = 0
    for possible in res[block].finditer(coils):
        log(f"Block of {block} could be at {possible.start()}")
        if possible.start() > 0:
            if coils[possible.start() - 1] == "#":
                log(f"Block preceded by # skipping")
                continue
            prefix = coils[: possible.start() - 1] + "."
        else:
            prefix = ""

        suffix = coils[possible.end() + block + 1 :]
        front = count_matches(prefix, pattern[:index], depth + 1)
        if front > 0:
            behind = count_matches(suffix, pattern[index + 1 :], depth + 1)
            increment = front * behind
            log(f"Found {increment} ways {front} * {behind}")
            count += increment
        else:
            log("No possible front, skipping", prefix, pattern[:index])
        log(f"Found {count} ways to match with {block} at {possible.start()}")
    return count


def process_line(line: str) -> int:
    start_time = time.monotonic()
    coils, pattern = parse_line(line)
    coils = ((coils + "?") * 5)[:-1]
    pattern = pattern * 5
    # print(f"\n{coils} <=> {pattern} --> ", end="", flush=True)
    count = count_matches(coils, pattern)
    # count = count_possible_matches(coils, pattern)
    # print(f"{count}", flush=True)
    elapsed = time.monotonic() - start_time
    if elapsed > 1:
        print(f'Slow {line} took {elapsed} | ("{line}", {count}),)')

    return count


def part2(input: list[str]) -> int:
    total = 0
    f = cached(process_line)
    for line in input:
        print(f"{line} => ", end="", flush=True)
        count = f(line)
        print(f"{count}", flush=True)
        total += count

    return total


if __name__ == "__main__":
    result = aoc.run_script(part2)
    print(f"Part 2: {result}")
