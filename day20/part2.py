#!/usr/bin/env python3
"""Advent of Code 2023 Day 20 Part 2"""

import functools
import itertools
import math
import re
import numpy


import aoc
from day20.part1 import *


def part2(data: list[str]) -> int:
    # By inspect "rx" gets input from one gate, the inputs to that gate
    # are on a cycle. So we need to find the cycle length of each input
    # and multiple together.
    circuit = build_circuit(parse_circuit(data))
    # We could just manually inspect the circuit to find the input to rx
    assert len(circuit["rx"].inputs) == 1, "Expected rx to have 1 input"
    watched_gate = list(circuit["rx"].inputs.keys())[0]
    press_count = {k: None for k in circuit[watched_gate].inputs}
    cycle_count = {k: None for k in circuit[watched_gate].inputs}

    presses = 0
    while not all(cycle_count.values()):
        presses += 1
        pulses = [("broadcast", "start button", False)]
        while pulses:
            gate, source, is_high = pulses.pop(0)
            if gate == "rx" and not is_high:
                # Doesn't happend unless we run for a few trillion cycles
                # but just in case ;)
                return presses + 1
            # Hard coding the fact that the watched gate is a conjunction
            # so we need to wait for all its inputs to go high so it will
            # send a low pulse.
            elif gate == watched_gate and is_high:
                if press_count[source] is not None:
                    cycle_length = presses - press_count[source]
                    cycle_count[source] = cycle_length
                press_count[source] = presses

            pulses.extend(circuit[gate].pulse(source, is_high))

    return math.prod(cycle_count.values())


if __name__ == "__main__":
    result = aoc.run_script(part2, day=20)
    print(f"Part 2: {result}")
