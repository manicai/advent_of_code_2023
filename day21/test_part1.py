import pytest
from day21.part1 import *

grid = [
    "...........",
    ".....###.#.",
    ".###.##..#.",
    "..#.#...#..",
    "....#.#....",
    ".##..S####.",
    ".##..#...#.",
    ".......##..",
    ".##.#.####.",
    ".##..##.##.",
    "...........",
]


def test_find_start():
    assert find_start(grid) == (5, 5)


@pytest.mark.parametrize(
    "row, col, expected",
    [
        (5, 5, {(5, 4), (4, 5)}),
        (5, 0, {(4, 0), (6, 0)}),
        (0, 0, {(0, 1), (1, 0)}),
        (7, 3, {(7, 2), (7, 4), (6, 3), (8, 3)}),
    ],
)
def test_neighbours(row, col, expected):
    actual = find_neighbours(grid, row, col)
    assert actual == expected


def test_find_locations_1():
    actual = find_locations(grid, 1)
    expected = {(5, 4), (4, 5)}
    assert actual == expected
