import sys

NAMES = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

assert NAMES[9] == "nine"


def lowest_found(a, b):
    # Lowest of two indices from `.find` ignoring -1
    if a == -1 and b == -1:
        return None
    elif a == -1:
        return b
    elif b == -1:
        return a
    else:
        return min(a, b)


def highest_found(a, b):
    # Highest of two indices from `.rfind` ignoring -1
    if a == -1 and b == -1:
        return None
    return max(a, b)


def find_numbers(line):
    """Find all the lowest and high index for the occurrence of
    each digit in a line of text."""
    indices = [None for _ in range(10)]
    for digit in range(10):
        l_numeric = line.find(str(digit))
        l_name = line.find(NAMES[digit])
        r_numeric = line.rfind(str(digit))
        r_name = line.rfind(NAMES[digit])
        indices[digit] = (
            lowest_found(l_name, l_numeric),
            highest_found(r_name, r_numeric),
        )
    return indices


in_path = sys.argv[1]
with open(in_path, "r") as in_file:
    total = 0
    for line in in_file.readlines():
        # print(line.strip(), end='\t')
        indices = find_numbers(line)
        # print(indices)

        first = None
        last = None
        for i, (min_i, max_i) in enumerate(indices):
            if min_i is None or max_i is None:
                assert min_i is None or max_i is None
                continue

            if first is None:
                first = (i, min_i)
            else:
                (value, index) = first
                if index > min_i:
                    first = (i, min_i)

            if last is None:
                last = (i, max_i)
            else:
                (value, index) = last
                if index < max_i:
                    last = (i, max_i)
        first_number, _ = first
        last_number, _ = last
        # print(first, last)

        calibration_value = first_number * 10 + last_number
        # print(calibration_value)
        total += calibration_value

    print(total)
