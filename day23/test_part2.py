import pytest
from day23.part2 import *


@pytest.mark.parametrize(
    "point, other, expected",
    [
        ((4, 3), (4, 4), True),
        ((4, 3), (5, 3), True),
        ((4, 4), (3, 3), False),
    ],
)
def test_is_adjacent(point, other, expected):
    actual = is_adjacent(point, other)
    assert actual == expected
