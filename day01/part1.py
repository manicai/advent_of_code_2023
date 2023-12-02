import sys

path = sys.argv[1]
with open(path, "r") as file:
    total = 0
    for line in file.readlines():
        digits = [int(char) for char in line if char.isdigit()]
        code = digits[0] * 10 + digits[-1]
        total += code

    print(total)
