import unittest

DIRECTIONS = [[1, 0], [0, 1], [-1, 0], [0, -1]]

def parse_input(input):
    return [[int(point) for point in list(line)] for line in input.strip().split("\n")]

def solve(input):
    map = parse_input(input)
    sum = 0
    for y, row in enumerate(map):
        for x, point in enumerate(row):
            lower = True
            for dir in DIRECTIONS:
                new_x = x + dir[0]
                new_y = y + dir[1]
                if ((new_y < 0) or (new_x < 0) or (new_y >= len(map)) or (new_x >= len(row))):
                    continue
                if map[new_y][new_x] <= point:
                    lower = False
            if lower:
                sum += point + 1
    return sum

def prod(sizes):
    basin_sizes = list(reversed(sorted(sizes)))
    prod = 1
    for n in range(0, 3):
        prod *= basin_sizes[n]
    return prod

def solve2(input):
    map = parse_input(input)

    seen = set()

    def search(point, basin_size):
        if point in seen:
            return basin_size

        seen.add(point)

        new_search_locations = []
        new_point_count = 1

        for dir in DIRECTIONS:
            new_x = point[0] + dir[0]
            new_y = point[1] + dir[1]
            if ((new_y < 0) or (new_x < 0) or (new_y >= len(map)) or (new_x >= len(map[0]))):
                continue
            if map[new_y][new_x] != 9:
                new_point_count += search((new_x, new_y), basin_size)

        return basin_size + new_point_count

    basin_sizes = []

    for y in range(0, len(map)):
        for x in range(0, len(map[0])):
            if (x, y) not in seen and map[y][x] != 9:
                basin_size = search((x, y), 0)
                basin_sizes.append(basin_size)

    return prod(basin_sizes)

with open("./input.txt") as f:
    input = f.read()

class Test(unittest.TestCase):

    def test_solve(self):
        self.assertEqual(solve(input), 562)

    def test_solve2(self):
        self.assertEqual(solve2(input), 1076922)

    def test_sample(self):
        self.assertEqual(solve(sample), 15)

    def test_sample2(self):
        self.assertEqual(solve2(sample), 1134)


sample = """2199943210
3987894921
9856789892
8767896789
9899965678"""

unittest.main()
