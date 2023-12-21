import pytest
from aoc.util import *


def test_to_ints():
    assert to_ints(["1", "3", "5"]) == [1, 3, 5]


def test_circular():
    l = "123"
    c = circular(l)
    assert l[0] == c[0]
    assert l[-1] == c[len(l) - 1]
    assert l[0] == c[len(l)]
    assert l[1] == c[100 * len(l) + 1]

    for a, b in zip(l, circular(l)):
        assert a == b
    assert len(l) == len(c)


def test_transpose():
    block = ["123", "456", "789"]
    assert transpose(block) == ["147", "258", "369"]


@pytest.mark.parametrize("n, expected", [
    (169, [13, 13]),
    (24, [2, 2, 2, 3]),
    (4, [2, 2]),
    (7, [7]),
    (131, [131]),
    (32, [2, 2, 2, 2, 2]),
])
def test_factorize(n, expected):
    assert factorize(n) == expected
