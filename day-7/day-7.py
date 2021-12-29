import unittest

def math(n):
    return sum([n for n in range(0, n + 1)])

def solve(input):
    crabs = [int(n) for n in input.split(",")]
    feul = 999999999
    for pos in range(min(crabs), max(crabs)):
        feul = min(feul, sum([abs(n - pos) for n in crabs]))
    return feul

def solve2(input):
    crabs = [int(n) for n in input.split(",")]
    feul = 999999999
    for pos in range(min(crabs), max(crabs)):
        feul = min(feul, sum([math(abs(n - pos)) for n in crabs]))
    return feul

with open("./input.txt") as f:
    input = f.read()

class Test(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(solve(sample), 37)

    def test_solve(self):
        self.assertEqual(solve(input), 348664)

    def test_sample2(self):
        self.assertEqual(solve2(sample), 168)

    def test_solve2(self):
        self.assertEqual(solve2(input), 100220525)

sample = "16,1,2,0,4,2,7,1,2,14"

unittest.main()
