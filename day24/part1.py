#!/usr/bin/env python3
"""Advent of Code 2023 Day 24 Part 1"""

import collections
import functools
import itertools
import math
import re
import numpy


import aoc


def in_zone(x, y):
    # bound_min, bound_max = 7, 27
    bound_min, bound_max = 200000000000000, 400000000000000
    return bound_min <= x <= bound_max and bound_min <= y <= bound_max


Particle = collections.namedtuple("Particle", ["position", "velocity"])


def parse_line(line):
    position, velocity = line.split("@")
    position = tuple(map(int, position.split(",")))
    velocity = tuple(map(int, velocity.split(",")))
    return Particle(position, velocity)


def part1(data: list[str]) -> int:
    particles = map(parse_line, data)

    count = 0
    for p, q in itertools.combinations(particles, 2):
        (p_x, p_y, _), (v_x, v_y, _) = p
        (q_x, q_y, _), (u_x, u_y, _) = q

        # print(f"Checking {p}, {q}")
        det = v_x * u_y - v_y * u_x
        if det == 0:
            # print(f"Parallel")
            continue

        t_q = (v_x * (p_y - q_y) - v_y * (p_x - q_x)) / det
        t_p = (u_x * (p_y - q_y) - u_y * (p_x - q_x)) / det
        if t_q < 0 or t_p < 0:
            # print(f"Crossed in past")
            continue

        x, y = (p_x + t_p * v_x, p_y + t_p * v_y)
        if in_zone(x, y):
            # print(f"Collision at {x}, {y}")
            count += 1
        else:
            # print("Collision outside zone")
            continue

    return count


if __name__ == "__main__":
    result = aoc.run_script(part1, day=24)
    print(f"Part 1: {result}")
