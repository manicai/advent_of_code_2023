import aoc

import functools
import itertools
import math
import numpy
import re


def parse_line(line: str) -> tuple[str, list[int]]:
    match = re.match(r"([?.#]+) ([0-9,]+)", line)
    try:
        return match.group(1), [int(x) for x in match.group(2).split(",")]
    except AttributeError:
        print(f"Failed to parse {line}")
        raise


def count_missing(coils: str, pattern: list[int]) -> int:
    total = sum(pattern)
    actual = coils.count("#")
    return total - actual


def find_matches(coils: str, pattern: list[int], depth=1) -> list[int]:
    # print(f"'{coils}' <=> {pattern}")
    if not pattern:  # Should be no more #s in coils
        if "#" in coils:
            return
        else:
            yield "." * len(coils)
            return
    if not coils and pattern:
        return

    prefix = re.match(r"[.]*", coils).end()
    coils = coils[prefix:]
    if not coils:
        return  # We've run out of coilsa
    # Three cases: either the coils starts with
    #  - a ? we will treat as a .
    #  - a ? we will treat as a #
    #  - a #
    if coils[0] == "?":
        for m in find_matches(coils[1:], pattern, depth=depth + 1):
            yield ("." * prefix) + "." + m

    head = pattern[0]
    # The correct number of ? or #s to match the pattern, then either
    # ?, . or the end of the string
    head_pattern = f"^([#?]{{{head}}})([?.]|$)"
    match = re.match(head_pattern, coils)
    if not match:
        return

    block = len(match.groups()[0])
    buffer = len(match.groups()[1])
    assert buffer == 1 or buffer == 0
    for m in find_matches(coils[block + buffer :], pattern[1:], depth=depth + 1):
        # print(match.groups())
        # print(f"{'.' * prefix} ==> {block} => {m}")
        result = ("." * prefix) + ("#" * block) + ("." * buffer) + m
        yield result


def count_possible_matches(coils: str, pattern: list[int]) -> int:
    count = len(list(find_matches(coils, pattern)))
    return count


def part1(input: list[str]) -> int:
    total = 0
    for line in input:
        coils, pattern = parse_line(line)
        count = count_possible_matches(coils, pattern)
        print(f"{coils} {pattern} {count}")
        total += count
    return total


if __name__ == "__main__":
    result = aoc.run_script(part1)
    print(f"Part 1: {result}")
