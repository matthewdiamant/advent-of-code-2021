import unittest

def parse_input(input):
    directions = [line.split(' ') for line in input.strip().split('\n')]
    return map(lambda direction: (direction[0], int(direction[1])), directions)

def solve_part_1(input):
    input = parse_input(input)
    h = 0
    d = 0
    for [direction, value] in input:
        if direction == 'up':
            d += -value
        if direction == 'down':
            d += value
        if direction == 'forward':
            h += value
    return h * d

def solve_part_2(input):
    input = parse_input(input)
    h = 0
    d = 0
    a = 0
    for [direction, value] in input:
        if direction == 'up':
            a -= value
        if direction == 'down':
            a += value
        if direction == 'forward':
            h += value
            d += a * value
    return h * d

with open("input.txt") as f:
    input = f.read()

class Test(unittest.TestCase):
    def test_solve_part_1(self):
        self.assertEqual(solve_part_1(input), 1868935)

    def test_solve_part_2(self):
        self.assertEqual(solve_part_2(input), 1965970888)

unittest.main()
