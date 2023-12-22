with open("../inputs/day_21/input.txt") as f:
    lines = f.readlines()

grid = [line.strip().replace("S", ".") for line in lines]

scale_by = 9

sideways = [r * scale_by for r in grid]
vertical = []
for _ in range(scale_by):
    vertical.extend(sideways.copy())

assert len(vertical) == len(vertical[0])
assert len(vertical) % 2 == 1
middle = (len(vertical) - 1) // 2
row = list(vertical[middle])
row[middle] = "S"
vertical[middle] = "".join(row)
assert vertical[middle].find("#") == -1

new_grid = ["".join(row) for row in vertical]

with open("test_large_grid.txt", "w") as f:
    f.write("\n".join(new_grid) + "\n")
