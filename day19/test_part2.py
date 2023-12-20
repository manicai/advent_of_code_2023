import pytest
from day19.part2 import *


@pytest.mark.parametrize(
    "part_set, expected",
    [
        ({"x": (1, 4000), "m": (1, 4000), "a": (1, 4000), "s": (1, 4000)}, 4000**4),
        ({"x": (1, 1), "m": (1, 1), "a": (1, 1), "s": (1, 1)}, 1),
        ({"x": (101, 110), "m": (201, 220), "a": (1001, 1030), "s": (1, 40)}, 240000),
    ],
)
def test_count_parts(part_set, expected):
    assert expected == count_parts(part_set)


def test_apply_rule_simple():
    parts = {"x": (1, 10), "m": (1, 10)}
    rule = [("x", "<", 6, "R"), ("*", "*", 1, "A")]
    received = list(apply_rule(rule, parts))
    assert ("R", {"x": (1, 5), "m": (1, 10)}) in received
    assert ("A", {"x": (6, 10), "m": (1, 10)}) in received


def test_apply_rule_less_simple():
    parts = {"x": (1, 10), "m": (1, 10)}
    rule = [("x", "<", 6, "fg"), ("m", ">", 8, "rt"), ("*", "*", 1, "A")]
    received = list(apply_rule(rule, parts))
    assert ("fg", {"x": (1, 5), "m": (1, 10)}) in received
    assert ("rt", {"x": (6, 10), "m": (9, 10)}) in received
