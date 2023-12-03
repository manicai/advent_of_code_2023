import sys


class Plan:
    def __init__(self, path):
        with open(path, "r") as fh:
            self._grid = [x.strip() for x in fh.readlines()]

    @property
    def row_count(self):
        return len(self._grid)

    @property
    def column_count(self):
        return len(self._grid[0])

    def __str__(self):
        return "\n".join(self._grid)

    def row(self, index):
        return self._grid[index]

    def at(self, row, col) -> str:
        # For ease put an imaginary boundary of '.' around the plan
        if row < 0 or row >= len(self._grid):
            return "."
        row_cells = self._grid[row]
        if col < 0 or col >= len(row_cells):
            return "."
        return row_cells[col]


def is_part(cell):
    if cell == ".":
        return False
    if cell.isdigit():
        return False
    return True


def is_symbol(plan, row_idx, start_col, end_col):
    neighbours = [(row_idx, start_col - 1), (row_idx, end_col + 1)]
    for col in range(start_col - 1, end_col + 2):
        neighbours.append((row_idx - 1, col))
        neighbours.append((row_idx + 1, col))

    for n_r, n_c in neighbours:
        if is_part(plan.at(n_r, n_c)):
            return True
    return False


def scan_row(plan, row_idx):
    values = []
    current = 0
    start_idx = None
    for i, v in enumerate(plan.row(row_idx)):
        if v.isdigit():
            current = 10 * current + int(v)
            if start_idx is None:
                assert current == int(v)
                start_idx = i
        else:
            if current != 0:  # Finished reading number
                symbol = is_symbol(plan, row_idx, start_idx, i - 1)
                values.append((current, symbol))
                start_idx = None
                current = 0
    return values


def find_symbols(plan):
    plan = Plan(in_path)
    symbols = []
    for row_idx in range(plan.row_count):
        values = scan_row(plan, row_idx)
        print(plan.row(row_idx), "->", values)
        symbols.extend(v for v, p in values if p)

    return symbols


if __name__ == "__main__":
    in_path = sys.argv[1]
    symbols = find_symbols(Plan(in_path))
    print(sum(symbols))
