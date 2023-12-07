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


def test():
    assert 13 == card_score('A')
    assert 0 == card_score('2'), card_score('2')
    assert hand_score('AAAAA') > hand_score('KKKKK')
    assert hand_score('AAAAA') > hand_score('AAAAK') # Five of a kind > four of a kind
    assert hand_score('22222') > hand_score('AAAAK') # Five of a kind > four of a kind
    assert hand_score('AAAAA') > hand_score('AKAAA') # Five of a kind > four of a kind
    assert hand_score('AAJAA') > hand_score('AAAKK') # Four of a kind > full house
    assert tie_break('KK677')  > tie_break('KTJJT')
    assert hand_score('KK677') > hand_score('KTJJT')
    assert hand_score('KKK77') > hand_score('KTJJT') # FH > two pair
    assert hand_score('KKK77') > hand_score('KJJJT') # FH > three of a kind
    assert hand_score('22245') > hand_score('KKQQT') # three of a kind > two pair
    assert hand_score('22TT3') > hand_score('AA893') # two pair > pair
    assert hand_score('22T93') > hand_score('AT893') # pair > all different
    assert hand_score('22K22') > hand_score('222K2') # tie break
    assert hand_score('32222') > hand_score('2K222') # tie break



if __name__ == "__main__":
    test()
    aoc.run_script(part1)
