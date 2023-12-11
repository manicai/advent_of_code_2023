from part2 import *
import pytest
from test_part1 import universe

expanded = [
    "..+#.+..+.",
    "..+..+.#+.",
    "#.+..+..+.",
    "++++++++++",
    "..+..+#.+.",
    ".#+..+..+.",
    "..+..+..+#",
    "++++++++++",
    "..+..+.#+.",
    "#.+.#+..+.",
    ]

def test_super_expand():
    result = super_expand_universe(universe)
    assert result == expanded


# ..+1.+..+.
# ..+..+.2+.
# 3.+..+..+.
# ++++++++++
# ..+..+4.+.
# .5+..+..+.
# ..+..+..+6
# ++++++++++
# ..+..+.7+.
# 8.+.9+..+.

def test_measure_distance():
    assert measure_distance((0, 0), (1, 1), expanded, 1) == 2
    assert measure_distance((0, 0), (1, 1), expanded, 100) == 2
    assert measure_distance((1, 1), (0, 0), expanded, 100) == 2

    # Crossing one expanded column: ..+0.
    assert measure_distance((0, 0), (0, 4), expanded, 1) == 4
    assert measure_distance((0, 0), (0, 4), expanded, 10) == 13

    # Crossing one expanded row: ..2+.
    assert measure_distance((0, 0,), (4, 0), expanded, 1) == 4
    assert measure_distance((0, 0,), (4, 0), expanded, 10) == 13
    assert measure_distance((0, 0,), (4, 0), expanded, 1000) == 1003

    # Symmetric
    assert measure_distance((4, 0,), (0, 0), expanded, 1000) == 1003