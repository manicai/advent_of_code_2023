import math
import sys
import typing

from part1 import *


def find_neighbours(plan, row_idx, col_idx):
    offsets = [-1, 0, 1]
    return [
        plan.at(row_idx + d_r, col_idx + d_c)
        for d_r in offsets
        for d_c in offsets
        if not (d_r == 0 and d_c == 0)
    ]


def number_starting_at(plan, row, col) -> typing.Optional[int]:
    if not plan.at(row, col).isdigit():
        return None
    v = 0
    while (x := plan.at(row, col)).isdigit():
        v = v * 10 + int(x)
        col += 1
    return v


def number_ending_at(plan, row, col) -> typing.Optional[int]:
    if not plan.at(row, col).isdigit():
        return None
    v = 0
    m = 1
    while (x := plan.at(row, col)).isdigit():
        v += int(x) * m
        m *= 10
        col -= 1
    return v


def find_neighbour_numbers(plan, row, col):
    numbers = [
        number_starting_at(plan, row, col + 1),  # to right
        number_ending_at(plan, row, col - 1),
    ]  # to left
    for offset in [-1, 1]:
        if plan.at(row + offset, col) == ".":
            # No number that goes straight across top/bottom. Any values must
            # be at a diagonal
            numbers.extend(
                [
                    number_starting_at(plan, row + offset, col + 1),  # to right
                    number_ending_at(plan, row + offset, col - 1),
                ]
            )
        else:
            # Have a number in same column move left to find where it starts
            start_col = col
            while plan.at(row + offset, start_col).isdigit():
                start_col -= 1
            start_col += 1  # step back to start.
            numbers.append(number_starting_at(plan, row + offset, start_col))

    return [n for n in numbers if n is not None]


def find_gears(plan):
    gears = []
    for r in range(plan.row_count):
        for c in range(plan.column_count):
            cell = plan.at(r, c)
            if cell != "*":
                continue

            neighbours = find_neighbours(plan, r, c)
            nn = find_neighbour_numbers(plan, r, c)
            is_gear = len(nn) == 2
            if not is_gear:
                continue
            ratio = math.prod(nn)
            # print(r, c, neighbours, nn, ratio)
            gears.append((r, c, nn, ratio))

    return gears


if __name__ == "__main__":
    p = Plan(sys.argv[1])
    gears = find_gears(p)
    print(sum(x[3] for x in gears))
