import unittest

def solve_part_1(input):
    count = 0
    for idx, x in enumerate(input[1:]):
        if x > input[idx]: count += 1
    return count

def solve_part_2(input):
    count = 0
    for idx, x in enumerate(input[3:]):
        if x > input[idx]: count += 1
    return count

with open('./input.txt') as f:
    input = map(int, [line for line in f.read().splitlines()])

class Test(unittest.TestCase):
    def test_solve_part_1_input(self):
        self.assertEqual(solve_part_1(input), 1832)

    def test_solve_part_2_input(self):
        self.assertEqual(solve_part_2(input), 1858)

unittest.main()
