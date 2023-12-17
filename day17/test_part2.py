import pytest
from day17.part2 import *
from day17.test_part1 import test_grid


@pytest.mark.parametrize(
    "node, expected",
    [
        ((0, 0, (0, 0), 0, 0), {(0, 4, (0, 1), 4, 12), (4, 0, (1, 0), 4, 13)}),
        ((0, 4, (0, 1), 4, 0), {(4, 4, (1, 0), 4, 17), (0, 5, (0, 1), 5, 3)}),
    ],
)
def test_neighbours(node, expected):
    neighbours = set(find_neighbours(node, test_grid))
    assert len(neighbours) == len(expected)
    assert neighbours == expected
