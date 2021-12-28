import unittest

def parse_input(input):
    lines = input.strip().split("\n")
    lines = [[[int(coord) for coord in coords.split(",")] for coords in line.split(" -> ")] for line in lines]
    return lines

def mark_grid(line, grid):
    [first, second] = line
    if second[1] - first[1] == 0:
        slope = (1, 0) if first[0] < second[0] else (-1, 0)
    elif second[0] - first[0] == 0:
        slope = (0, 1) if first[1] < second[1] else (0, -1)
    else:
        y = (second[1] - first[1]) // abs(second[1] - first[1])
        x = (second[0] - first[0]) // abs(second[0] - first[0])
        slope = (x, y)
    i = 0
    x, y = first
    while [x - slope[0], y - slope[1]] != second:
        grid[(x, y)] = grid[(x, y)] + 1 if (x, y) in grid else 1
        x += slope[0]
        y += slope[1]

    return grid

def output(grid):
    max_x = 0
    max_y = 0
    for cell in grid:
        if cell[0] > max_x:
            max_x = cell[0]
        if cell[1] > max_y:
            max_y = cell[1]
    output = ""
    for y in range(0, max_y):
        for x in range(0, max_x):
            output += str(grid[(x, y)]) if (x, y) in grid else "."
        output += "\n"
    print(output)

def solve(input):
    grid = dict()
    lines = parse_input(input)
    for line in lines:
        [first, second] = line
        if first[0] == second[0] or first[1] == second[1]:
            mark_grid(line, grid)
    sum = 0
    for cell in grid.values():
        if cell > 1:
            sum += 1
    return sum

def solve2(input):
    grid = dict()
    lines = parse_input(input)
    for line in lines:
        [first, second] = line
        if first[0] == second[0] or first[1] == second[1] or abs((first[0] - second[0]) / (first[1] - second[1])) == 1:
            mark_grid(line, grid)

    sum = 0
    for cell in grid.values():
        if cell > 1:
            sum += 1
    return sum

with open("./input.txt") as f:
    input = f.read()

class Test(unittest.TestCase):
    def test_mark_grid(self):
        line = [[1, 1], [1, 3]]
        self.assertEqual(mark_grid(line, {}), {(1, 1): 1, (1, 2): 1, (1, 3): 1})
        line = [[9, 7], [7, 7]]
        self.assertEqual(mark_grid(line, {}), {(7, 7): 1, (8, 7): 1, (9, 7): 1})
        line = [[7, 9], [5, 7]]
        self.assertEqual(mark_grid(line, {}), {(5, 7): 1, (6, 8): 1, (7, 9): 1})
        line = [[5, 9], [7, 7]]
        self.assertEqual(mark_grid(line, {}), {(5, 9): 1, (6, 8): 1, (7, 7): 1})

    def test_solve_sample(self):
        self.assertEqual(solve(sample), 5)

    def test_solve2_sample(self):
        self.assertEqual(solve2(sample), 12)

    def test_solve(self):
        self.assertEqual(solve(input), 7142)
        pass

    def test_solve2(self):
        self.assertEqual(solve2(input), 20012)
        pass

sample = """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2"""

unittest.main()
