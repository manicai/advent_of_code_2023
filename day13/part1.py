import aoc
import aoc.lib

import functools
import itertools
import math
import numpy
import re


def read_blocks(input: list[str]) -> list[list[str]]:
    blocks = []
    current = []
    for line in input:
        if line == "":
            blocks.append(current)
            current = []
        else:
            current.append(line)
    if current:
        blocks.append(current)
    return blocks


def check_vertical(block: list[str], candidate: int) -> bool:
    assert (
        block[candidate] == block[candidate + 1]
    ), f"Row {candidate} is not symmetrical {block[candidate]} != {block[candidate - 1]}"
    offset = 1
    while candidate - offset >= 0 and candidate + 1 + offset < len(block):
        if block[candidate - offset] != block[candidate + 1 + offset]:
            return False
        offset += 1
    return True


def find_vertical_symmetry(block: list[str]) -> int:
    possible = []
    for i, row in enumerate(block[:-1]):
        if row == block[i + 1]:
            possible.append(i)
    if not possible:
        return []

    # print(f"Possible vertical symmetry rows: {possible}")
    confirmed = []
    for r in possible:
        if check_vertical(block, r):
            confirmed.append(r)

    return confirmed


def find_horizontal_symmetry(block: list[str]) -> int:
    t = aoc.lib.transpose(block)
    return find_vertical_symmetry(t)


def print_block(block: list[str]):
    print("-" * 40)
    for row in block:
        print(row)
    print("-" * 40)
    print()


def part1(input: list[str]) -> int:
    blocks = read_blocks(input)
    total = 0
    for block in blocks:
        # print_block(block)
        hsym = find_horizontal_symmetry(block)
        vsym = find_vertical_symmetry(block)
        assert len(hsym) < 2, f"Multiple horizontal symmetries {hsym}"
        assert len(vsym) < 2, f"Multiple vertical symmetries {vsym}"
        # print(hsym, vsym)
        value = sum((h + 1) for h in hsym) + sum(100 * (v + 1) for v in vsym)
        total += value

    return total


if __name__ == "__main__":
    result = aoc.run_script(part1, day=13)
    print(f"Part 1: {result}")
