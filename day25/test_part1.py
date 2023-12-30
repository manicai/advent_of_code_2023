import pytest
from day25.part1 import *


def test_min_cut():
    edges = []
    partition_size = 5
    for i in range(partition_size):
        for j in range(i + 1, partition_size):
            edges.append((f"A{i}", f"A{j}"))
            edges.append((f"B{i}", f"B{j}"))
    edges.append(("A0", "B0"))
    edges.append(("A1", "B1"))

    cut, partition = repeat_karger(edges, n=500, target_size=2)
    assert len(cut) == 2
    assert ("A0", "B0") in cut
    assert ("A1", "B1") in cut
    assert {f"A{i}" for i in range(partition_size)} in partition
    assert {f"B{i}" for i in range(partition_size)} in partition
