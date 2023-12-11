from .part1 import *


def test():
    assert 13 == card_score("A")
    assert 0 == card_score("2"), card_score("2")
    assert hand_score("AAAAA") > hand_score("KKKKK")
    assert hand_score("AAAAA") > hand_score("AAAAK")  # Five of a kind > four of a kind
    assert hand_score("22222") > hand_score("AAAAK")  # Five of a kind > four of a kind
    assert hand_score("AAAAA") > hand_score("AKAAA")  # Five of a kind > four of a kind
    assert hand_score("AAJAA") > hand_score("AAAKK")  # Four of a kind > full house
    assert tie_break("KK677") > tie_break("KTJJT")
    assert hand_score("KK677") > hand_score("KTJJT")
    assert hand_score("KKK77") > hand_score("KTJJT")  # FH > two pair
    assert hand_score("KKK77") > hand_score("KJJJT")  # FH > three of a kind
    assert hand_score("22245") > hand_score("KKQQT")  # three of a kind > two pair
    assert hand_score("22TT3") > hand_score("AA893")  # two pair > pair
    assert hand_score("22T93") > hand_score("AT893")  # pair > all different
    assert hand_score("22K22") > hand_score("222K2")  # tie break
    assert hand_score("32222") > hand_score("2K222")  # tie break
