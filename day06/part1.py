import aoc

import functools
import itertools
import math
import re


def load_races(input):
    times = aoc.to_ints(input[0][len("Time:") :].split())
    distances = aoc.to_ints(input[1][len("Distance:") :].split())
    return list(zip(times, distances))


def count_wins(race_time, record):
    def distance(hold_time):
        return hold_time * (race_time - hold_time)

    return len([i for i in range(race_time) if distance(i) > record])


def part1(input):
    races = load_races(input)
    count = 1
    for time, distance in races:
        wins = count_wins(time, distance)
        print(time, distance, wins)
        count *= wins
    print(count)


if __name__ == "__main__":
    aoc.run_script(part1)
