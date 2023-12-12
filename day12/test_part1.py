from .part1 import *
import pytest


@pytest.mark.parametrize(
    "line,expected",
    [
        ("???.### 1,1,3", ("???.###", [1, 1, 3])),
        (".??..??...?##. 1,1,3", (".??..??...?##.", [1, 1, 3])),
        ("????.######..#####. 1,6,5", ("????.######..#####.", [1, 6, 5])),
    ],
)
def test_parse_line(line, expected):
    assert expected == parse_line(line)


@pytest.mark.parametrize(
    "coils, pattern, missing",
    [
        ("???.###", [1, 1, 3], 2),
        (".??..??...?##.", [1, 1, 3], 3),
        ("????.######..#####.", [1, 6, 5], 1),
    ],
)
def test_count_missing(coils, pattern, missing):
    assert missing == count_missing(coils, pattern)


@pytest.mark.parametrize(
    "coils, pattern, matches",
    [
        ("...", [], ["..."]),
        ("???", [], ["..."]),
        (".#.", [], []),
        (".#.", [1], [".#."]),
        ("?.#.", [1], ["..#."]),
        ("?.?.", [1], ["#...", "..#."]),
        ("???.###", [1, 1, 3], ["#.#.###"]),
        (
            ".??..??...?##.",
            [1, 1, 3],
            [".#...#....###.", ".#....#...###.", "..#..#....###.", "..#...#...###."],
        ),
        (
            "?###????????",
            [3, 2, 1],
            [
                ".###.##.#...",
                ".###.##..#..",
                ".###.##...#.",
                ".###.##....#",
                ".###..##.#..",
                ".###..##..#.",
                ".###..##...#",
                ".###...##.#.",
                ".###...##..#",
                ".###....##.#",
            ],
        ),
    ],
)
def test_find_matches(coils, pattern, matches):
    found = list(find_matches(coils, pattern))
    if len(found) > 10:
        for f in found:
            print(f)
    for f in found:
        assert f in matches, found
    for m in matches:
        assert m in found
