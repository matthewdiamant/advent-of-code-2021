import unittest

def parse_input(input):
    return [[char for char in line] for line in input.split("\n")]

def output(map):
    return "\n".join(["".join(line) for line in map])

def epoch(old_map):
    map = [[char for char in line] for line in old_map]
    max_x = len(map[0])
    max_y = len(map)
    frozen = set()
    for y, line in enumerate(map):
        for x, space in enumerate(line):
            if ((x, y) in frozen or ((x + 1) % max_x, y) in frozen):
                continue
            if space == ">":
                next_space = map[y][(x + 1) % max_x]
                if (next_space == "."):
                    map[y][(x + 1) % max_x] = ">"
                    map[y][x] = "."
                    frozen.add(((x + 1) % max_x, y))
                    frozen.add((x, y))
                else:
                    map[y][x] = ">"
    frozen = set()
    for y, line in enumerate(map):
        for x, space in enumerate(line):
            if ((x, y) in frozen or (x, (y + 1) % max_y) in frozen):
                continue
            if space == "v":
                next_space = map[(y + 1) % max_y][x]
                if (next_space == "."):
                    map[(y + 1) % max_y][x] = "v"
                    map[y][x] = "."
                    frozen.add((x, (y + 1) % max_y))
                    frozen.add((x, y))
                else:
                    map[y][x] = "v"
    return map

def solve(input):
    map = parse_input(input)
    return output(epoch(map))

def solve_n(input, n):
    map = parse_input(input)
    for _ in range(0, n):
        new_map = epoch(map)
        map = new_map
    return output(map)

def solve2(input):
    map = parse_input(input)
    iterations = 0
    while True:
        new_map = epoch(map)
        iterations += 1
        if output(map) == output(new_map):
            return iterations
        map = new_map

with open("./input.txt") as f:
    input = f.read()

sample1 = "...>>>>>..."

sample2 = """..........
.>v....v..
.......>..
.........."""

sample3 = """...>...
.......
......>
v.....>
......>
.......
..vvv.."""

big_sample = """v...>>.vv>
.vv>>.vv..
>>.>v>...v
>>v>>.>.v.
v>v.vv.v..
>.>>..v...
.vv..>.>v.
v.v..>>v.v
....v..v.>"""

class Test(unittest.TestCase):
    def test_solve_sample1(self):
        self.assertEqual(solve(sample1), "...>>>>.>..")

    def test_solve_sample2(self):
        self.assertEqual(solve(sample2), """..........
.>........
..v....v>.
..........""")

    def test_solve_sample3(self):
        self.assertEqual(solve(sample3), """..vv>..
.......
>......
v.....>
>......
.......
....v..""")

    def test_solve_big_sample(self):
        self.assertEqual(solve(big_sample), """....>.>v.>
v.v>.>v.v.
>v>>..>v..
>>v>v>.>.v
.>v.v...v.
v>>.>vvv..
..v...>>..
vv...>>vv.
>.v.v..v.v""")

    def test_solve_big_sample(self):
        self.assertEqual(solve_n(big_sample, 2), """>.v.v>>..v
v.v.>>vv..
>v>.>.>.v.
>>v>v.>v>.
.>..v....v
.>v>>.v.v.
v....v>v>.
.vv..>>v..
v>.....vv.""")

    def test_solve(self):
        self.assertEqual(solve2(input.strip()), 305)

unittest.main()
