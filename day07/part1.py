import aoc

import collections
import functools
import itertools
import math
import re

cards = 'AKQJT987654332'

def card_score(card):
    return 13 - cards.index(card)

pattern_score = {
    (5,): 800,
    (1,4): 700,
    (2,3): 600,
    (1,1,3): 500,
    (1,2,2): 400,
    (1,1,1,2): 300,
    (1,1,1,1,1): 200,
}

def hand_score(hand):
    tie_breaker = sum(card_score(c) + 13 * (4 - i) for i, c in enumerate(hand))
    counts = collections.defaultdict(lambda: 0)
    for c in hand:
        counts[c] += 1
    pattern = tuple(sorted(counts.values()))
    print(counts.values(), pattern, pattern_score[pattern])
    


def part1(input):
    for line in input:
        print(line, line.split(' '), len(line.split(' ')))
        hand, bet = line.split(' ')
        print(hand)
        hand_score(hand)


def test():
    assert 13 == card_score('A')
    assert 0 == card_score('2'), card_score('2')

if __name__ == "__main__":
    test()
    aoc.run_script(part1)
