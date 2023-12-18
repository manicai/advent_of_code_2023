def to_ints(lst):
    return [int(n) for n in lst]


def transpose(block: list[str]) -> list[str]:
    return ["".join(row[i] for row in block) for i in range(len(block[0]))]


def circular(lst):
    class CircularView:
        def __init__(self):
            self._len = len(lst)
            assert self._len != 0

        def __getitem__(self, key):
            return lst[key % self._len]

        def __len__(self):
            return self._len

    return CircularView()


def print_grid(grid: list[str]):
    for row in grid:
        print(row)


# Row / Column co-ordinates.
NORTH = (-1, 0)
SOUTH = (1, 0)
EAST = (0, 1)
WEST = (0, -1)
