import pytest
from day25.part1 import *


def test_min_cut():
    edges = []
    for i in range(5):
        for j in range(i + 1, 5):
            edges.append((f"A{i}", f"A{j}"))
            edges.append((f"B{i}", f"B{j}"))
    edges.append(("A0", "B0"))
    edges.append(("A1", "B1"))

    cut = repeat_karger(edges)
    print(cut)
    assert False
