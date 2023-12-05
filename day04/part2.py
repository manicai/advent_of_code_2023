from aoc import run_script


def process_line(line):
    card, numbers = line.split(":")
    winning, have = numbers.split("|")
    winning = set(winning.split())
    have = set(have.split())
    # print(card, winning, have)
    matches = winning.intersection(have)
    score = 2 ** (len(matches) - 1) if matches else 0
    # print(matches, score)
    return card, winning, have, matches, score


def count_cards(lines):
    # print("\n".join(lines))
    count = [1 for _ in range(len(lines))]
    for i, line in enumerate(lines):
        _, _, _, matches, score = process_line(line)
        # print(line.strip(), len(matches))
        match_count = len(matches)
        for add in range(i + 1, i + 1 + match_count):
            count[add] += count[i]

    # print(count)
    print(sum(count))
    return sum(count)


if __name__ == "__main__":
    run_script(count_cards)
