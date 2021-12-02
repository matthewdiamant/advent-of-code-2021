import unittest

def parse_input(input):
    directions = [line.split(' ') for line in input.strip().split('\n')]
    return map(lambda direction: (direction[0], int(direction[1])), directions)

def solve_part_1(input):
    input = parse_input(input)
    horizontal = 0
    depth = 0
    for [direction, value] in input:
        if direction == 'up':
            depth -= value
        if direction == 'down':
            depth += value
        if direction == 'forward':
            horizontal += value
    return horizontal * depth

def solve_part_2(input):
    input = parse_input(input)
    horizontal = 0
    depth = 0
    aim = 0
    for [direction, value] in input:
        if direction == 'up':
            aim -= value
        if direction == 'down':
            aim += value
        if direction == 'forward':
            horizontal += value
            depth += aim * value
    return horizontal * depth

with open("input.txt") as f:
    input = f.read()

class Test(unittest.TestCase):
    def test_solve_part_1(self):
        self.assertEqual(solve_part_1(input), 1868935)

    def test_solve_part_2(self):
        self.assertEqual(solve_part_2(input), 1965970888)

unittest.main()
