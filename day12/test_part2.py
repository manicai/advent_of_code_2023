from day12.part2 import *
import pytest


@pytest.mark.parametrize(
    "coils, count, expected",
    [
        ("???", 2, 2),
        ("????", 2, 3),
        ("???", 3, 1),
        ("?#??", 2, 1),
        ("?#??", 3, 2),
        ("?.??", 2, 2),
        ("?.?#", 2, 0),
        ("#.#.", 2, 0),
        (".#.?.", 2, 1),
        (".???.", 2, 3),
        ("?.#.", 2, 1),
    ],
)
def test_count_options(coils, count, expected):
    actual = count_options(coils, count)
    assert actual == expected


@pytest.mark.parametrize(
    "coils, pattern, expected",
    [
        (".???", [], 1),
        (".#.", [1], 1),
        ("....", [1], 0),
        (".?....", [1], 1),
        (".#.?..", [1], 1),
        (".?.?..", [1], 2),
        (".?...?", [1], 2),
        ("???.###", [1, 1, 3], 1),
        ("????.#...#...?????.#...#...", [4, 1, 1, 4, 1, 1], 2),
        (".??..??...?##.", [1, 1, 3], 4),
        ("???", [2], 2),
        ("###????", [3, 2], 2),
        ("?###????????", [3, 2, 1], 10),
        ("??????", [2, 1], 6),
        ("?#?#?#?#?#?#?#?", [1, 3, 1, 6], 1),
        ("???????##?", [1, 5], 7),
        ("???????##?????????##?", [1, 5, 1, 5], 98),
        (".?????????????.", [1, 1], 66),
        ("???#...????#", [1, 1, 1, 1], 7),
        ("??.#...???.#", [1, 1, 1, 1], 7),
        ("??#.", [2], 1),
    ],
)
def test_count_matches(coils, pattern, expected):
    # print(list(find_matches(coils, pattern)))
    result = count_matches(coils, pattern)
    assert result == expected


@pytest.mark.parametrize("coils, pivot, pivot_len, expected", [("???.###", 2, 2, True)])
def test_pivot_possible(coils, pivot, pivot_len, expected):
    assert pivot_possible(coils, pivot, pivot_len) == expected
