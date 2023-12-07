import aoc
import part1

import collections
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



def process_line(line):
    hand, bet = line.split(' ')
    return hand, hand_score(hand), int(bet)


def hand_score(hand):
    counts = collections.defaultdict(lambda: 0)
    joker_count = 0
    for c in hand:
        if c == 'J':
            joker_count += 1
        else:
            counts[c] += 1
    if joker_count < 5:
        pattern = list(sorted(counts.values()))
        try:
            pattern[-1] += joker_count
        except IndexError:
            print(pattern, joker_count)
            raise
    else:
        pattern = [5]
    pattern = tuple(pattern)
    # print(counts.values(), pattern, part1.pattern_score[pattern])
    # print(part1.pattern_score[pattern] + tie_break(hand))
    return part1.pattern_score[pattern] + tie_break(hand)


def part2(input):
    hands = [process_line(line) for line in input]
    hands.sort(key=lambda x: x[1])
    total = 0
    assert len(hands) == len(set(x[1] for x in hands)), "No duplicate scores"
    assert len(hands) == len(set(x[0] for x in hands)), "No duplicate hands"
    # assert len(hands) == 1000
    for rank, (hand, score, bet) in enumerate(hands):
        assert bet > 0
        total += bet * (rank + 1)
        # print(rank + 1, hand, score, bet, total)
    print(total)


if __name__ == "__main__":
    aoc.run_script(part2)
