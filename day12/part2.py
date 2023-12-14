import aoc

import functools
import itertools
import math
import numpy
import re
import time


def parse_line(line: str) -> tuple[str, list[int]]:
    match = re.match(r"([?.#]+) ([0-9,]+)", line)
    try:
        return match.group(1), [int(x) for x in match.group(2).split(",")]
    except AttributeError:
        print(f"Failed to parse {line}")
        raise


@functools.cache
def pivot_possible(coils: str, pivot_location: int, pivot_len: int) -> bool:
    try:
        for i in range(pivot_location, pivot_location + pivot_len - 1):
            if coils[i] == ".":  # # or ? is okay
                return False
        if coils[pivot_location + pivot_len - 1] == "#":  # . or ? is okay
            return False
    except IndexError:
        return False
        # print("IndexError", coils, pivot_location, pivot_len)
        # raise
    return True


@functools.cache
def count_options(coils: str, block_len: int) -> int:
    def can_start_block_at(start):
        for i in range(block_len - 1):
            if coils[start + i] == ".":  # has to be # or ?
                return False
        if coils[start + block_len - 1] == "#":  # has to be . or ?
            return False
        for i in range(start + block_len, len(coils)):  # No # after the block
            if coils[i] == "#":
                return False
        for i in range(start):  # No # before the block
            if coils[i] == "#":
                return False
        return True

    coils = coils.lstrip(".")
    if block_len > len(coils):
        return 0
    elif coils.count("#") >= block_len:
        return 0
    elif coils[-1] == "#":
        return 0
    return sum(
        1 for start in range(len(coils) - block_len + 1) if can_start_block_at(start)
    )


def recursive_count(coils: str, pattern: list[int], depth=0) -> int:
    # print ("  " * depth, f"coils={coils}, pattern={pattern}")
    if coils == "??.#.":
        # breakpoint()
        pass
    if not pattern:
        return 0 if "#" in coils else 1
    if len(pattern) == 1:
        count = count_options(coils, pattern[0])
        # print("  " * depth, f"coils={coils}, pattern={pattern} counted {count}")
        return count

    pivot = len(pattern) // 2
    # print("  " * depth, f"pivot={pivot} ")
    prefix = pattern[:pivot]
    suffix = pattern[pivot + 1 :]

    pivot_len = pattern[pivot]
    min_prefix_len = sum(prefix)
    min_suffix_len = pivot_len + sum(suffix)

    min_pivot_position = min_prefix_len
    max_pivot_position = len(coils) - min_suffix_len + 1
    # breakpoint()
    # print(
    #     "  " * depth,
    #     f"{coils} {pattern} =>",
    #     f"({min_prefix_len} : {prefix}) -> ",
    #     f" pivot at [{min_pivot_position}, {max_pivot_position}] ->",
    #     f"({min_suffix_len}: {suffix})",
    # )
    counts = 0
    for pivot_location in range(min_pivot_position, max_pivot_position + 1):
        # print("  " * depth, f"pivot_location={pivot_location}")
        if not pivot_possible(coils, pivot_location, pivot_len):
            # print("  " * depth, f"pivot not possible")
            continue

        # print("  " * depth, f"Prefix => {coils[:pivot_location]}, {prefix}")
        prefix_count = recursive_count(coils[:pivot_location], prefix, depth + 1)

        # print("  " * depth, f"Suffix => {coils[pivot_location + pivot_len:]}, {suffix}")
        suffix_count = recursive_count(
            coils[pivot_location + pivot_len :], suffix, depth + 1
        )
        # print("  " * depth, f"{prefix_count} * {suffix_count}")
        counts += prefix_count * suffix_count

    # print ("  " * depth, f"coils={coils}, pattern={pattern} => {counts}")
    return counts


def count_matches(coils: str, pattern: list[int]) -> int:
    # print(f"'{coils}' <=> {pattern}")
    # Remove all duplicate .s as they are redundant, also
    # remove start and end "." but add one to the end
    # to match the last blocks.
    shortened = re.sub(r"[.]+", ".", coils.strip(".")) + "."
    # Include the end . in each block
    pattern_with_dots = [b + 1 for b in pattern]
    return recursive_count(shortened, pattern_with_dots)


def process_line(line: str) -> int:
    coils, pattern = parse_line(line)
    coils = "?".join([coils] * 5)
    pattern = pattern * 5
    return count_matches(coils, pattern)


def part2(input: list[str]) -> int:
    total = 0
    for line in input:
        # print(f"{line} => ", end="", flush=True)
        # start_time = time.monotonic()
        count = process_line(line)
        # elapsed = time.monotonic() - start_time
        # print(f"{count} ({elapsed})", flush=True)

        total += count

    return total


if __name__ == "__main__":
    # This was the worst pattern for my original version
    # print(count_matches("?#????????#???.????", [2, 1, 2, 2, 1, 2]))
    # print(process_line("?#????????#???.???? 2,1,2,2,1,2"))
    result = aoc.run_script(part2)
    print(f"Part 2: {result}")
