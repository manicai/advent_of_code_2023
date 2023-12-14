from .part2 import *
import pytest


@pytest.mark.parametrize(
    "line, expected",
    [
        (".....", "....."),
        ("...O.", "....O"),
        ("..O.O", "...OO"),
        (".#.O.", ".#..O"),
        ("O#..O", "O#..O"),
        ("OO.O.O..##", "....OOOO##"),
        ("...OO....O", ".......OOO"),
        (".O...#O..O", "....O#..OO"),
    ],
)
def test_roll_east(line, expected):
    actual = roll_row_east(line)
    assert actual == expected


def test_cycle():
    grid = [
        "O....#....",
        "O.OO#....#",
        ".....##...",
        "OO.#O....O",
        ".O.....O#.",
        "O.#..O.#.#",
        "..O..#O..O",
        ".......O..",
        "#....###..",
        "#OO..#....",
    ]
    expected_1 = [
        ".....#....",
        "....#...O#",
        "...OO##...",
        ".OO#......",
        ".....OOO#.",
        ".O#...O#.#",
        "....O#....",
        "......OOOO",
        "#...O###..",
        "#..OO#....",
    ]
    result = cycle(grid)
    assert result == expected_1
    expected_2 = [
        ".....#....",
        "....#...O#",
        ".....##...",
        "..O#......",
        ".....OOO#.",
        ".O#...O#.#",
        "....O#...O",
        ".......OOO",
        "#..OO###..",
        "#.OOO#...O",
    ]

    result = cycle(result)
    assert result == expected_2

    expected_3 = [
        ".....#....",
        "....#...O#",
        ".....##...",
        "..O#......",
        ".....OOO#.",
        ".O#...O#.#",
        "....O#...O",
        ".......OOO",
        "#...O###.O",
        "#.OOO#...O",
    ]

    result = cycle(result)
    assert result == expected_3


def test_run_cycle():
    grid = [
        "O....#....",
        "O.OO#....#",
        ".....##...",
        "OO.#O....O",
        ".O.....O#.",
        "O.#..O.#.#",
        "..O..#O..O",
        ".......O..",
        "#....###..",
        "#OO..#....",
    ]
    for c in range(15):
        cycled = run_cycle(grid, 1000_000_000 + c)
        print(score(cycled))
    cycled = run_cycle(grid, 1000_000_000)
    assert score(cycled) == 64
