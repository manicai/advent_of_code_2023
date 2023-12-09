from part1 import *
import pytest


def test():
    assert extrapolate([0,0,0,0,0]) == 0
    assert extrapolate([3,3,3,3,3]) == 3
    assert extrapolate([1,2,3,4,5]) == 6
    assert extrapolate([11,13,16,20,25]) == 31
    # Problem article examples ...
    assert extrapolate([0, 3, 6, 9, 12, 15]) == 18
    assert extrapolate([1, 3, 6, 10, 15, 21]) == 28
    assert extrapolate([10, 13, 16, 21, 30, 45]) == 68
