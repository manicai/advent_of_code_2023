from aoc import run_script

def process_line(line):
    card, numbers = line.split(':')
    winning, have = numbers.split('|')
    winning = set(winning.split())
    have = set(have.split())
    #print(card, winning, have)
    matches = winning.intersection(have)
    score = 2 ** (len(matches) - 1) if matches else 0
    # print(matches, score)
    return card, winning, have, score

def find_scores(lines):
    print('\n'.join(lines))
    total = 0
    for line in lines:
        _, _, _, score = process_line(line)
        # print(line.strip(), score)
        total += score
    print(total)
    return total

if __name__ == '__main__':
    run_script(find_scores)
