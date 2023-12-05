import aoc

import functools
import itertools
import math
import re

class LazyMapRange:
    def __init__(self, key_start, value_start, length):
        self.key_start = key_start
        self.value_start = value_start
        self.length = length

    def contains(self, key):
        return key >= self.key_start and key < (self.key_start + self.length)

    def value_for(self, key):
        assert self.contains(key)
        offset = key - self.key_start
        return self.value_start + offset

class LazyMap:
    def __init__(self):
        self.ranges = []

    def add_range(self, lr):
        self.ranges.append(lr)

    def _find_range(self, key):
        matching = [r for r in self.ranges if r.contains(key)]
        assert len(matching) < 2
        return matching[0] if matching else None

    def contains(self, key):
        return self._find_range(key) is not None
    
    def value_for(self, key):
        r = self._find_range(key)
        assert r
        return r.value_for(key)


def part1(input):
    pass

def test():
    lmr = LazyMapRange(10, 20, 5)
    assert not lmr.contains(9)
    assert lmr.contains(10)
    assert lmr.contains(14)
    assert not lmr.contains(15)
    assert lmr.value_for(10) == 20
    assert lmr.value_for(14) == 24
    
    lm = LazyMap()
    lm.add_range(lmr)
    lm.add_range(LazyMapRange(100, 200, 100))
    assert not lm.contains(9)
    assert lm.contains(10)
    assert lm.contains(14)
    assert not lm.contains(15)
    assert lm.value_for(10) == 20
    assert lm.value_for(14) == 24
    assert not lm.contains(99)
    assert lm.contains(199)
    assert lm.value_for(199) == 299
    assert lm.value_for(150) == 250

if __name__ == '__main__':
    test()
    aoc.run_script(part1)
