#!/usr/bin/env python3
"""Solution to Day 12, Part 2 of Advent of Code 2013.

Version 2 using dynamic programming."""
import aoc

from day12.part1 import parse_line


def count(coils: str, pattern: list[int], coil_index: int, pattern_index: int, current_block_length: int, accumulator='') -> int:
    counter = 0
    for cell in ['#', '.']:
        if coil_index == len(coils):
            print(f"{accumulator}")
            return 1

        current = coils[coil_index]
        # Can't add a spring if we've hit a space or vice versa.
        if current != cell and current != '?':
            continue

        if cell == '#':
            # Extend the current block
            counter += count(coils, pattern, coil_index + 1, pattern_index, current_block_length + 1, accumulator + cell)
        elif cell == '.':
            # End the current block if we are in one
            if current_block_length > 0:
                # Abort if we're trying to match against a block and we've
                # run out of them.
                if pattern_index >= len(pattern):
                    return 0
                # Similarly, abort if the current block length doesn't match
                pattern_block_length = pattern[pattern_index]
                if current_block_length != pattern_block_length:
                    return 0
                # Otherwise, keep going.
                counter += count(coils, pattern, coil_index + 1, pattern_index + 1, 0, accumulator + cell)
            # otherwise keep going along to the next spring.
            else:
                counter += count(coils, pattern, coil_index + 1, pattern_index, current_block_length, accumulator + cell)

    return counter



def count_matches(coils: str, pattern: list[int]) -> int:
    print(coils, pattern)
    return count(coils, pattern, 0, 0, 0)


def process_line(line: str) -> int:
    coils, pattern = parse_line(line)
    return count_matches("?".join([coils] * 5), pattern * 5)


def part2(input: list[str]) -> int:
    return sum(process_line(line) for line in input)


if __name__ == "__main__":
    result = aoc.run_script(part2)
    print(f"Part 2: {result}")
