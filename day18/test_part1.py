import pytest
from day18.part1 import *

example = [
    "R 6 (#70c710)",
    "D 5 (#0dc571)",
    "L 2 (#5713f0)",
    "D 2 (#d2c081)",
    "R 2 (#59c680)",
    "D 2 (#411b91)",
    "L 5 (#8ceee2)",
    "U 2 (#caa173)",
    "L 1 (#1b58a2)",
    "U 2 (#caa171)",
    "R 2 (#7807d2)",
    "U 3 (#a77fa3)",
    "L 2 (#015232)",
    "U 2 (#7a21e3)",
]


def test_find_bounds():
    bounds = find_bounds(example)
    assert bounds.east_west == (0, 6)
    assert bounds.south_north == (0, 9)


def test_shade_grid():
    input_grid = [
        list("###..###..###"),
        list("#.#..#.#..#.#"),
        list("#.####.####.#"),
        list("#...........#"),
        list("#...#####...#"),
        list("#####...#####"),
    ]
    expected_grid = [
        list("###..###..###"),
        list("###..###..###"),
        list("#############"),
        list("#############"),
        list("#############"),
        list("#####...#####"),
    ]
    actual = shade_grid(input_grid)
    # print_grid(actual)
    assert actual == expected_grid
