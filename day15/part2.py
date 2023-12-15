import aoc
from day15.part1 import holiday_hash

import collections
import functools
import itertools
import math
import numpy
import re


def print_hash_map(hm):
    print("Hash Map: {")
    for i, m in enumerate(hm):
        if m:
            print("  ", i, m)
    print("}")


def part2(input: list[str]) -> int:
    line = input[0]
    hash_map = [collections.OrderedDict() for _ in range(256)]
    for instruction in line.split(","):
        # print(instruction)
        m = re.match(r"(\w+)([-]|[=](\d+))", instruction)
        label, operation, value = m.groups()
        label_hash = holiday_hash(label)
        if operation == "-":
            if label in hash_map[label_hash]:
                del hash_map[label_hash][label]
        else:
            assert operation.startswith("=") and value is not None
            hash_map[label_hash][label] = int(value)
        # print_hash_map(hash_map)

    return sum(
        (box_index + 1) * sum((i + 1) * v for i, v in enumerate(box.values()))
        for box_index, box in enumerate(hash_map)
    )


if __name__ == "__main__":
    result = aoc.run_script(part2)
    print(f"Part 2: {result}")
