#!/usr/bin/env python3
"""Advent of Code 2023 Day 19 Part 2"""

import functools
import itertools
import math
import re
import numpy


import aoc
import day19.part1 as part1


def parse_rule(rule: str):
    if m := re.match(r"([xmas])([<>])(\d+):(\w+)", rule):
        selector = m.group(1)
        op = m.group(2)
        value = int(m.group(3))
        action = m.group(4)
        return (selector, op, value, action)

    assert re.match(r"\w+", rule)
    return ("*", "*", 0, rule)


def parse(lines: list[str]):
    rules = {}
    for line in lines:
        if not line:
            continue
        if (m := re.match(r"(\w+)\{([a-zA-Z0-9:<>,]+)\}", line)) is not None:
            rule_name = m.group(1)
            rules[rule_name] = [parse_rule(step) for step in m.group(2).split(",")]
        else:
            # Part information not relevant for part 2
            pass

    return rules


def apply_rule(rule, part_set):
    # print(rule)
    # print(part_set)
    selector, op, value, next = rule[0]
    if selector == "*":
        # Match everything remaining.
        yield (next, part_set)
    else:
        current_min, current_max = part_set[selector]
        assert current_min <= current_max, "Range got corrupted"
        if op == "<":
            if current_min >= value:  # Nothing matches
                return
            elif current_max < value:
                yield (next, part_set)  # Everything matches
            else:  # Split the range
                matching_range = (current_min, value - 1)
                matched_part_set = part_set.copy()
                matched_part_set[selector] = matching_range
                yield (next, matched_part_set)

                remaining_range = (value, current_max)
                remaining_part_set = part_set.copy()
                remaining_part_set[
                    selector
                ] = remaining_range  # Functional might be better here?
                for result in apply_rule(rule[1:], remaining_part_set):
                    yield result
        else:
            assert op == ">", f"Unknown operator {op}"
            if current_max <= value:
                return  # Nothing matches
            if current_min > value:
                yield (next, part_set)  # Everything matches
            else:  # Split the range
                matching_range = (value + 1, current_max)
                matched_part_set = part_set.copy()
                matched_part_set[selector] = matching_range
                yield (next, matched_part_set)

                remaining_range = (current_min, value)
                remaining_part_set = part_set.copy()
                remaining_part_set[
                    selector
                ] = remaining_range  # Functional might be better here?
                for result in apply_rule(rule[1:], remaining_part_set):
                    yield result


def count_parts(part_set):
    count = 1
    for r in part_set.values():
        count *= r[1] - r[0] + 1
    return count


def part2(data: list[str]) -> int:
    rules = parse(data)

    start = ("in", {"x": (1, 4000), "m": (1, 4000), "a": (1, 4000), "s": (1, 4000)})
    accepted = []
    pending = [start]
    while pending:
        rule, part_set = pending.pop()
        # print(rule, part_set)
        rule_defn = rules[rule]
        for next_rule, new_part_set in apply_rule(rule_defn, part_set):
            if next_rule == "A":
                accepted.append(new_part_set)
            elif next_rule == "R":
                pass  # Rejected, we can just forget about this set.
            else:
                pending.append((next_rule, new_part_set))

    return sum(count_parts(part_set) for part_set in accepted)


if __name__ == "__main__":
    result = aoc.run_script(part2, day=19)
    print(f"Part 2: {result}")
