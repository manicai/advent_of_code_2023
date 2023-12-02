import sys

path = sys.argv[1]
with open(path, 'r') as f:
    total = 0
    for l in f.readlines():
        digits = [int(c) for c in l.strip() if c.isdigit()]
        code = digits[0] * 10 + digits[-1]
        total += code
    
    print(total)
    