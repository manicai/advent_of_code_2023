import aoc
import part1

import functools
import itertools
import math
import re

cards = "AKQT987654332J"


def card_score(card):
    return 13 - cards.index(card)


def tie_break(hand):
    t = sum(card_score(c) * 14 ** (4 - i) for i, c in enumerate(hand))
    assert t < 1_000_000
    return t


def hand_score(hand):
    return tie_break(hand)


def part2(input):
    pass


if __name__ == "__main__":
    aoc.run_script(part2)
