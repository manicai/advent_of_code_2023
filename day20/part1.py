#!/usr/bin/env python3
"""Advent of Code 2023 Day 20 Part 1"""

import functools
import itertools
import math
import re
import numpy


import aoc


class Gate:
    def __init__(self, name, outputs):
        self.name = name
        self.outputs = outputs
        self.inputs = {}

    def pulse(self, source, is_high) -> list[tuple[str, str, bool]]:
        raise NotImplementedError

    def add_input(self, gate):
        if gate in self.inputs:
            return
        self.inputs[gate] = False

    def __repr__(self) -> str:
        return str(self)


class Broadcaster(Gate):
    def __init__(self, name, outputs):
        super().__init__(name, outputs)

    def add_input(self, gate):
        assert False, "Broadcaster cannot have inputs"

    def pulse(self, source, is_high) -> list[tuple[str, str, bool]]:
        return [(output, self.name, is_high) for output in self.outputs]

    def __str__(self) -> str:
        return "broadcast -> " + ", ".join(self.outputs)


class FlipFlop(Gate):
    def __init__(self, name, outputs):
        super().__init__(name, outputs)
        self.state = False

    def pulse(self, _ignore_source, is_high) -> list[tuple[str, str, bool]]:
        if is_high:
            return []  # Ignore high pulses

        self.state = not self.state
        return [(output, self.name, self.state) for output in self.outputs]

    def __str__(self) -> str:
        return f"'%{self.name} -> {', '.join(self.outputs)}'"


class Conjunction(Gate):
    def __init__(self, name, outputs):
        super().__init__(name, outputs)
        self.inputs = {}

    def pulse(self, source, is_high) -> list[tuple[str, str, bool]]:
        assert source in self.inputs, f"Unknown source {source} for {self.name}"
        self.inputs[source] = is_high
        if all(self.inputs.values()):
            return [(output, self.name, False) for output in self.outputs]
        else:
            return [(output, self.name, True) for output in self.outputs]

    def add_input(self, gate):
        assert gate not in self.inputs, f"Gate {gate} already in {self.inputs}"
        self.inputs[gate] = False

    def __str__(self) -> str:
        return f"'&{self.name} -> {', '.join(self.outputs)}'"


class Sink(Gate):
    def __init__(self, name, outputs):
        super().__init__(name, outputs)

    def pulse(self, source, is_high) -> list[tuple[str, str, bool]]:
        # Just swallows the pulse
        return []

    def __str__(self) -> str:
        return f"!{self.name}"


def parse_circuit(lines: list[str]):
    gates = {}
    for line in lines:
        gate, output = line.split(" -> ")
        outputs = output.split(", ")
        if gate == "broadcaster":
            gates["broadcast"] = ("broadcast", outputs)
        else:
            assert gate[0] == "%" or gate[0] == "&"
            gate_type = gate[0]
            gate_name = gate[1:]
            gates[gate_name] = (gate_type, outputs)
    return gates


def build_circuit(gates: dict[str, tuple[str, list[str]]]):
    circuit = {}
    for name, (gate_type, outputs) in gates.items():
        if gate_type == "%":
            circuit[name] = FlipFlop(name, outputs)
        elif gate_type == "&":
            circuit[name] = Conjunction(name, outputs)
        elif gate_type == "broadcast":
            circuit[name] = Broadcaster(name, outputs)
        else:
            assert False, "Unknown gate type"

    for name, (_, outputs) in gates.items():
        for output in outputs:
            if output not in circuit:
                # We only find out about sinks because they are listed
                # as the output of another gate
                circuit[output] = Sink(output, [])
            circuit[output].add_input(name)

    return circuit


def part1(data: list[str]) -> int:
    circuit = build_circuit(parse_circuit(data))
    counts = {True: 0, False: 0}
    for _ in range(1000):
        pulses = [("broadcast", "start button", False)]
        while pulses:
            gate, source, is_high = pulses.pop(0)
            counts[is_high] += 1
            pulses.extend(circuit[gate].pulse(source, is_high))

    return counts[True] * counts[False]


if __name__ == "__main__":
    result = aoc.run_script(part1, day=20)
    print(f"Part 1: {result}")
