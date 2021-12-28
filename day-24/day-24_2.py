from functools import cache
import unittest

with open("./input.txt") as f:
    input = f.read()

ops = [line.split() for line in input.strip().split("\n")]

@cache
def search(op_index, w, x, y, z, range):
    if z > 10**7:
        return (False, '')

    if op_index >= len(ops):
        return (z == 0, '')

    values = { 'w': w, 'x': x, 'y': y, 'z': z }

    op = ops[op_index]

    if op[0] == 'inp':
        for d in range:
            result = search(op_index + 1, d, values['x'], values['y'], values['z'], range)

            if result[0]:
                return (True, str(d) + result[1])

        return (False, 0)

    second = values[op[2]] if op[2] in values else int(op[2])

    if op[0] == 'add':
        values[op[1]] += second
    if op[0] == 'mul':
        values[op[1]] *= second
    if op[0] == 'div':
        values[op[1]] //= second
    if op[0] == 'mod':
        values[op[1]] %= second
    if op[0] == 'eql':
        values[op[1]] = 1 if second == values[op[1]] else 0

    return search(op_index + 1, values['w'], values['x'], values['y'], values['z'], range)

class Test(unittest.TestCase):
    def test_solve_part1(self):
        self.assertEqual(search(0, 0, 0, 0, 0, range(9, 0, -1)), (True, '91398299697996'))

    def test_solve_part2(self):
        self.assertEqual(search(0, 0, 0, 0, 0, range(1, 10)), (True, '41171183141291'))

unittest.main()
