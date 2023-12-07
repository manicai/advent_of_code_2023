from part2 import *


def test_part2():
    assert hand_score("32T3K") < hand_score("KK677")
    assert hand_score("KK677") < hand_score("KTJJT")
    assert hand_score("KK677") < hand_score("T55J5")
    assert hand_score("KK677") < hand_score("QQQJA")
    assert hand_score("T55J5") < hand_score("QQQJA")
    assert hand_score("QQQJA") < hand_score("KTJJT")
