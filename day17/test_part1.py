import pytest
from day17.part1 import *

test_grid = [
    "2413432311323",
    "3215453535623",
    "3255245654254",
    "3446585845452",
    "4546657867536",
    "1438598798454",
    "4457876987766",
    "3637877979653",
    "4654967986887",
    "4564679986453",
    "1224686865563",
    "2546548887735",
    "4322674655533",
]


@pytest.mark.parametrize(
    "node, expected",
    [
        ((0, 0, (0, 0), 0), {(0, 1, (0, 1), 1), (1, 0, (1, 0), 1)}),
        ((0, 3, (0, 1), 3), {(0, 2, (0, -1), 1), (1, 3, (1, 0), 1)}),
        (
            (1, 1, (0, 1), 1),
            {
                (1, 2, (0, 1), 2),
                (0, 1, (-1, 0), 1),
                (2, 1, (1, 0), 1),
                (1, 0, (0, -1), 1),
            },
        ),
    ],
)
def test_neighbours(node, expected):
    neighbours = set(find_neighbours(node, test_grid))
    assert len(neighbours) == len(expected)
    assert neighbours == expected
