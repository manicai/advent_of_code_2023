import pytest
from day21.part2 import calculate, calculate2

with open("../inputs/day_21/input.txt") as f:
    grid = [r.strip() for r in f.readlines()]


@pytest.mark.parametrize(
    "tiles, expected",
    [
        (0, 3889),
        (2, 95591),
        (4, 309181),
    ],
)
def test(tiles, expected):
    steps = tiles * 131 + 65
    actual = calculate2(grid, tiles)
    print(f"Actual: {actual} Expected: {expected} Difference {actual - expected}")
    assert actual == expected
