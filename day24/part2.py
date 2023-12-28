#!/usr/bin/env python3
"""Advent of Code 2023 Day 24 Part 2"""

import collections
import functools
import itertools
import math
import re
import numpy as np


import aoc
import aoc.util
from day24.part1 import parse_line, Particle


class Particle:
    def __init__(self, position, velocity):
        self.position = np.array(position)
        self.velocity = np.array(velocity)

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f"Particle({self.position}, {self.velocity})"

    def __hash__(self):
        return hash((self.position, self.velocity))

    def at(self, time):
        return self.position + self.velocity * time


# "(x_0 - x_1) + (u_0 - u_1) * t + (u_r - u_1) * delta_1",
# "(y_0 - y_1) + (v_0 - v_1) * t + (v_r - v_1) * delta_1",
# "(z_0 - z_1) + (w_0 - w_1) * t + (w_r - w_1) * delta_1",
# "(x_0 - x_2) + (u_0 - u_2) * t + (u_r - u_2) * delta_2",
# "(y_0 - y_2) + (v_0 - v_2) * t + (v_r - v_2) * delta_2",
# "(z_0 - z_2) + (w_0 - w_2) * t + (w_r - w_2) * delta_2",


def solve_given_vr_wr(particle1, particle2, v_r, w_r):
    (x_0, y_0, z_0), (u_0, v_0, w_0) = particle1.position, particle1.velocity
    (x_1, y_1, z_1), (u_1, v_1, w_1) = particle2.position, particle2.velocity

    A = y_0 - y_1
    B = v_0 - v_1
    C = v_r - v_1
    D = z_0 - z_1
    E = w_0 - w_1
    F = w_r - w_1

    demoninator = B * F - C * E
    numerator = -(A * F - D * C)
    if demoninator == 0 or numerator % demoninator != 0:
        return False, None, None, None

    t = numerator // demoninator
    if t < 0:
        return False, None, None, None

    demoninator = C * E - B * F
    numerator = -(A * E - D * B)
    if demoninator == 0 or numerator % demoninator != 0:
        return False, None, None, None
    delta_1 = numerator // demoninator
    if (t + delta_1) < 0:
        return False, None, None, None

    u_r = x_1 + u_1 * (t + delta_1) - x_0 - u_0 * t
    if u_r % delta_1 != 0:
        return False, None, None, None
    u_r //= delta_1

    return True, t, delta_1, u_r


def check_collides(rock, hailstone):
    (h_x, h_y, h_z), (u_r, v_r, w_r) = hailstone.position, hailstone.velocity
    (r_x, r_y, r_z), (u_rock, v_rock, w_rock) = rock.position, rock.velocity

    # print(f"Checking {i} at {t + delta_1} {rock}, {particles[1]}")
    times = [None, None, None]
    for dimension in range(3):
        if rock.velocity[dimension] == hailstone.velocity[dimension]:
            # If velocities are the same, they will never collide unless
            # start positions are the same.
            if rock.position[dimension] != hailstone.position[dimension]:
                return False
        else:
            n = hailstone.position[0] - rock.position[0]
            d = rock.velocity[0] - hailstone.velocity[0]
            if n % d != 0:
                return False
            times[dimension] = n // d
            if times[dimension] < 0:
                return False

    times = [t for t in times if t is not None]
    for i in range(len(times) - 1):
        if times[i] != times[i + 1]:
            return False
    return True


def part2(data: list[str]) -> int:
    hailstones = [Particle(*parse_line(line)) for line in data]
    RANGE_SIZE = 500
    for v_r in range(-RANGE_SIZE, RANGE_SIZE):
        for w_r in range(-RANGE_SIZE, RANGE_SIZE):
            solved, t, delta_1, u_r = solve_given_vr_wr(
                hailstones[0], hailstones[1], v_r, w_r
            )
            if not solved:
                continue
            # print(f"Found {u_r} {v_r} {w_r} colliding at {t} then {delta_1} ")

            p_x, p_y, p_z = hailstones[0].at(t)
            h_x = p_x - u_r * t
            h_y = p_y - v_r * t
            h_z = p_z - w_r * t
            rock = Particle((h_x, h_y, h_z), (u_r, v_r, w_r))

            for i in range(3):
                assert rock.at(t)[i] == hailstones[0].at(t)[i]
                # print(f"Checking {i} at {t + delta_1} {rock}, {particles[1]}")
                assert (
                    rock.at(t + delta_1)[i] == hailstones[1].at(t + delta_1)[i]
                ), f"{i} {rock.at(t + delta_1)[i]} != {hailstones[1].at(t + delta_1)[i]}"

            all_collide = True
            for stone in hailstones:
                if not check_collides(rock, stone):
                    all_collide = False
                    break
            if not all_collide:
                continue

            print(rock)
            # print(sum(rock.position))
            return sum(rock.position)

    # min_x = min(p.position[0] for p in particles)
    # min_y = min(p.position[1] for p in particles)
    # min_z = min(p.position[2] for p in particles)
    # for p in particles:
    #     print(p.position[0] / min_x, p.position[1] / min_y, p.position[2] / min_z)

    # print(min(p.velocity[0] for p in particles), max(p.velocity[0] for p in particles))
    # print(min(p.velocity[1] for p in particles), max(p.velocity[1] for p in particles))
    # print(min(p.velocity[2] for p in particles), max(p.velocity[2] for p in particles))


if __name__ == "__main__":
    result = aoc.run_script(part2, day=24)
    print(f"Part 2: {result}")
