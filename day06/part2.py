import aoc
import part1

import functools
import itertools
import math
import re


def part2(input):
    # Don't really need to bother parsing so manual entry
    time = 58819676
    distance = 434104122191218
    print(part1.count_wins(time, distance))


if __name__ == "__main__":
    aoc.run_script(part2)
