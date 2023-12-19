#!/usr/bin/env python3
"""Advent of Code 2023 Day 19 Part 1"""

import functools
import itertools
import math
import operator
import re
import numpy


import aoc


def parse_rule(rule: str):
    if m := re.match(r"([xmas])([<>])(\d+):(\w+)", rule):
        selector = m.group(1)
        if m.group(2) == "<":
            op = operator.lt
        else:
            assert m.group(2) == ">"
            op = operator.gt
        value = int(m.group(3))
        action = m.group(4)
        return (selector, op, value, action)

    assert re.match(r"\w+", rule)
    return ("x", lambda x, y: True, 0, rule)


def parse(lines: list[str]):
    rules = {}
    parts = []
    for line in lines:
        if not line:
            continue
        if (m := re.match(r"(\w+)\{([a-zA-Z0-9:<>,]+)\}", line)) is not None:
            rule_name = m.group(1)
            rules[rule_name] = [parse_rule(step) for step in m.group(2).split(",")]
        else:
            assert line[0] == "{" and line[-1] == "}"
            parts.append(
                dict(
                    (attribute[0], int(attribute[2:]))
                    for attribute in line[1:-1].split(",")
                )
            )

    return rules, parts


def apply_rules(rules, part):
    # print(part, ":", end=" ")
    rule = "in"
    # chain = []
    while rule != "A" and rule != "R":
        # chain.append(rule)
        for step in rules[rule]:
            selector, op, value, action = step
            if op(part[selector], value):
                rule = action
                break

    # chain.append(rule)
    # print(" -> ".join(chain))
    return rule == "A"


def score_part(part):
    return sum(part.values())


def part1(data: list[str]) -> int:
    rules, parts = parse(data)
    return sum(score_part(part) for part in parts if apply_rules(rules, part))


if __name__ == "__main__":
    result = aoc.run_script(part1, day=19)
    print(f"Part 1: {result}")
