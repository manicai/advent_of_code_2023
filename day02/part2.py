import math
import sys

from part1 import parse_draws

with open(sys.argv[1], 'r', encoding='ascii') as fh:
    total = 0
    
    for line in fh.readlines():
        game, draws = line.strip().split(':')
        game_number = int(game[5:])
        draws = parse_draws(draws)        

        combined = {}
        for draw in draws:
            for ball, count in draw.items():    
                combined.setdefault(ball, []).append(count)

        highest = {}
        for ball in combined:
            highest[ball] = max(combined[ball])
        # print(game_number, combined, highest)

        power = math.prod(highest.values())
        # print(power)
        total += power
    
    print(f'----\n{total}')