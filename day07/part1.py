import aoc

import collections
import functools
import itertools
import math
import re

cards = 'AKQJT987654332'

def card_score(card):
    # assert card in cards, card
    return 13 - cards.index(card)

pattern_score = {
    (5,):        8_000_000,
    (1,4):       7_000_000,
    (2,3):       6_000_000,
    (1,1,3):     5_000_000,
    (1,2,2):     4_000_000,
    (1,1,1,2):   3_000_000,
    (1,1,1,1,1): 2_000_000,
}

def tie_break(hand):
    t = sum(card_score(c) * 14 ** (4 - i) for i, c in enumerate(hand))
    assert t < 1_000_000
    return t


def hand_score(hand):
    counts = collections.defaultdict(lambda: 0)
    for c in hand:
        counts[c] += 1
    pattern = tuple(sorted(counts.values()))
    print(counts.values(), pattern, pattern_score[pattern])
    print(pattern_score[pattern] + tie_break(hand))
    return pattern_score[pattern] + tie_break(hand)


def process_line(line):
    hand, bet = line.split(' ')
    return hand, hand_score(hand), int(bet)


def compare_hands(lhs, rhs):
    return lhs[1] > rhs[1]


def part1(input):
    hands = [process_line(line) for line in input]
    hands.sort(key=lambda x: x[1])
    total = 0
    assert len(hands) == len(set(x[1] for x in hands)), "No duplicate scores"
    assert len(hands) == len(set(x[0] for x in hands)), "No duplicate hands"
    assert len(hands) == 1000
    for rank, (hand, score, bet) in enumerate(hands):
        assert bet > 0
        total += bet * (rank + 1)
        print(rank + 1, hand, score, bet, total)
    print(total)


if __name__ == "__main__":
    test()
    aoc.run_script(part1)
