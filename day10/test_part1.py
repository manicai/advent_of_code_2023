from part1 import *
import pytest

simple = [
    ".....",
    ".S-7.",
    ".|.|.",
    ".L-J.",
    ".....",
]

example = [
    "..F7.",
    ".FJ|.",
    "SJ.L7",
    "|F--J",
    "LJ...",
]


@pytest.mark.parametrize("grid, location", [(simple, (1, 1)), (example, (2, 0))])
def test_find_start(grid, location):
    assert find_start(grid) == location


j_start = ["F-7", "L-S"]
dash_start = ["FS7", "L-S"]
bar_start = ["F7", "|S", "LJ"]
l_start = ["F7", "SJ"]
seven_start = ["FS.", "|L7", "L-J"]


@pytest.mark.parametrize(
    "grid, correct_start",
    [
        (simple, "F"),
        (example, "F"),
        (j_start, "J"),
        (dash_start, "-"),
        (bar_start, "|"),
        (l_start, "L"),
        (seven_start, "7"),
    ],
)
def test_infer_start(grid, correct_start):
    start = find_start(grid)
    cell = infer_start_cell(grid, start)
    assert correct_start == cell


@pytest.mark.parametrize(
    "location, cell",
    [
        ((0, 0), "."),
        ((1, 1), "F"),
        ((2, 1), "J"),
        ((2, 0), "S"),
        ((3, 4), "J"),
        ((-1, 3), "."),
    ],
)
def test_at(location, cell):
    assert at(example, location) == cell


def attached_neighbours():
    for cell, steps in neighbours.items():
        for step in steps:
            assert cell in ATTACHED[step]

    for step, cells in ATTACHED.items():
        for cell in cells:
            assert step in neighbours[cell]


@pytest.mark.parametrize(
    "grid, length", [(l_start, 2), (j_start, 3), (simple, 4), (example, 8)]
)
def test_trace_route(grid, length):
    assert length == part1(grid)
