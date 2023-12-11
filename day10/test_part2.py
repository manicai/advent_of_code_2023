from .part2 import *
import pytest

from day10.test_part1 import simple, example


example_dirty = [
    "7LF7-",
    "-FJ|7",
    "SJ-L7",
    "|F--J",
    "LJ-LF",
]


@pytest.mark.parametrize(
    "dirty, clean", [(simple, simple), (example, example), (example_dirty, example)]
)
def test_scrub_map(dirty, clean):
    route = trace_route(dirty)
    assert clean == scrub_map(dirty, route)


simple_specified = [
    ".....",
    ".F-7.",
    ".|.|.",
    ".L-J.",
    ".....",
]


def test_specify_start():
    specified = specify_start(simple)
    assert simple_specified == specified


simple_expanded = [
    "..." "..." "..." "..." "...",
    "..." "..." "..." "..." "...",
    "..." "..." "..." "..." "...",
    "..." "..." "..." "..." "...",
    "..." ".F-" "---" "-7." "...",
    "..." ".|." "..." ".|." "...",
    "..." ".|." "..." ".|." "...",
    "..." ".|." "..." ".|." "...",
    "..." ".|." "..." ".|." "...",
    "..." ".|." "..." ".|." "...",
    "..." ".L-" "---" "-J." "...",
    "..." "..." "..." "..." "...",
    "..." "..." "..." "..." "...",
    "..." "..." "..." "..." "...",
    "..." "..." "..." "..." "...",
]


def test_expand():
    expanded = expand_map(simple_specified)
    assert len(expanded) == 3 * len(simple_specified)
    assert len(expanded) == len(simple_expanded)
    assert all(len(r) == 15 for r in expanded)
    for expected, received in zip(simple_expanded, expanded):
        assert expected == received


def test_shrink():
    shrunk = shrink_map(simple_expanded)
    for expected, received in zip(simple_specified, shrunk):
        assert expected == received
