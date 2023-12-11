from .part1 import *
import pytest


def test_findall():
    assert find_all("01234", "5") == []
    assert find_all("012345", "5") == [5]
    assert find_all("0123455", "5") == [5, 6]
    assert find_all("501234555", "5") == [0, 6, 7, 8]


universe = [
    "...#......",
    ".......#..",
    "#.........",
    "..........",
    "......#...",
    ".#........",
    ".........#",
    "..........",
    ".......#..",
    "#...#.....",
]

expanded_universe = [
    "....#........",
    ".........#...",
    "#............",
    ".............",
    ".............",
    "........#....",
    ".#...........",
    "............#",
    ".............",
    ".............",
    ".........#...",
    "#....#.......",
]


def test_expand():
    calculated = expand_universe(universe)
    assert calculated == expanded_universe
