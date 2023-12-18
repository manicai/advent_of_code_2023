import pytest
from aoc.lib import *


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
