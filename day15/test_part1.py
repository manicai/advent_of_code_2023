from .part1 import *
import pytest


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ("HASH", 52),
        ("rn=1", 30),
        ("cm-", 253),
        ("qp=3", 97),
        ("cm=2", 47),
        ("qp-", 14),
        ("pc=4", 180),
        ("ot=9", 9),
        ("ab=5", 197),
        ("pc-", 48),
        ("pc=6", 214),
        ("ot=7", 231),
    ],
)
def test_holiday_hash(test_input, expected):
    actual = holiday_hash(test_input)
    assert actual == expected


def test_hash_line():
    actual = holiday_hash_line("rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7")
    assert actual == 1320
