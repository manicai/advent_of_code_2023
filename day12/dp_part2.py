#!/usr/bin/env python3
"""Solution to Day 12, Part 2 of Advent of Code 2013.

Version 2 using dynamic programming."""
import aoc

from day12.part1 import parse_line


def count_matches(coils: str, pattern: list[int]) -> int:
    return 0


def process_line(line: str) -> int:
    coils, pattern = parse_line(line)
    return count_matches("?".join([coils] * 5), pattern * 5)


def part2(input: list[str]) -> int:
    return sum(process_line(line) for line in input)


if __name__ == "__main__":
    result = aoc.run_script(part2)
    print(f"Part 2: {result}")
