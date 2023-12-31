import aoc
import aoc.util

try:
    from . import part1
except ImportError:
    import part1

import functools
import itertools
import math
import numpy
import re


def check_vertical(block: list[str], candidate: int) -> bool:
    assert (
        count_differences(block[candidate], block[candidate + 1]) <= 1
    ), f"Row {candidate} is not symmetrical {block[candidate]} != {block[candidate - 1]}"
    offset = 0
    off_by_ones = 0
    while candidate - offset >= 0 and candidate + 1 + offset < len(block):
        bottom = block[candidate - offset]
        top = block[candidate + 1 + offset]
        if top != bottom:
            differences = count_differences(top, bottom)
            assert differences > 0
            if differences == 1:
                off_by_ones += 1
                # print(f"Off by one at {offset}")
            if differences > 1:
                return False
        offset += 1
    return off_by_ones == 1


def count_differences(a: str, b: str) -> int:
    if a == b:
        return 0
    assert len(a) == len(b)
    count = 0
    for c_a, c_b in zip(a, b):
        if c_a != c_b:
            count += 1
    return count


def find_vertical_symmetry(block: list[str]) -> int:
    possible = []
    for i, row in enumerate(block[:-1]):
        if count_differences(row, block[i + 1]) <= 1:
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
    t = aoc.util.transpose(block)
    return find_vertical_symmetry(t)


def print_block(block: list[str]):
    print("-" * 40)
    for row in block:
        print(row)
    print("-" * 40)
    print()


def part2(input: list[str]) -> int:
    blocks = part1.read_blocks(input)
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
    result = aoc.run_script(part2, day=13)
    print(f"Part 2: {result}")
