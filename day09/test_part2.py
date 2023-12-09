from part2 import *
import pytest


def test():
    assert back_extrapolate([0, 0, 0, 0, 0]) == 0
    assert back_extrapolate([3, 3, 3, 3, 3]) == 3
    assert back_extrapolate([1, 2, 3, 4, 5]) == 0
    assert back_extrapolate([11, 13, 16, 20, 25]) == 10
    # Problem article examples ...
    assert back_extrapolate([0, 3, 6, 9, 12, 15]) == -3
    assert back_extrapolate([1, 3, 6, 10, 15, 21]) == 0
    assert back_extrapolate([10, 13, 16, 21, 30, 45]) == 5
