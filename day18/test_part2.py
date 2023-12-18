import pytest
from day18.part2 import *


@pytest.mark.parametrize(
    "locations, expected",
    [
        ([(0, 0), (0, 1), (1, 1), (1, 0), (0, 0)], 1),
        ([(0, 0), (0, 1), (1, 1), (1, 2), (2, 2), (2, 0), (0, 0)], 3),
    ],
)
def test_shoe_lace(locations, expected):
    area = shoe_lace(locations)
    assert area == expected
