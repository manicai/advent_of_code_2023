import sys

max_counts = {
    "red": 12,
    "green": 13,
    "blue": 14,
}


def parse_draw(draw):
    counts = dict(
        (colour, int(count))
        for (count, colour) in [tuple(ball.strip().split()) for ball in draw.split(",")]
    )
    return counts


def parse_draws(draws):
    return [parse_draw(draw) for draw in draws.split(";")]


def is_possible(draw):
    for colour, count in draw.items():
        if count > max_counts[colour]:
            return False
    return True


def all_true(iter):
    for i in iter:
        if not i:
            return False
    return True


if __name__ == "__main__":
    with open(sys.argv[1], "r", encoding="ascii") as fh:
        total = 0
        for line in fh.readlines():
            game, draws = line.strip().split(":")
            game_number = int(game[5:])
            draws = parse_draws(draws)
            possible = all_true(is_possible(draw) for draw in draws)
            print(game_number, draws, possible)
            if possible:
                total += game_number

        print(total)
