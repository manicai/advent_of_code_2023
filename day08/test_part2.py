from part2 import *
import pytest


def test_factors():
    assert find_factors(144) == [2, 2, 2, 2, 3, 3]
    assert find_factors(13) == [13]
    assert find_factors(169) == [13, 13]
    assert find_factors(256) == [2] * 8

    assert lowest_common_multiple([4, 5]) == 20
    assert lowest_common_multiple([4, 8]) == 8
    assert lowest_common_multiple([12, 20]) == 60
    assert lowest_common_multiple([12, 20, 7]) == 60 * 7
