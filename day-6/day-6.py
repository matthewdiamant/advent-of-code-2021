import sys
import unittest

class School:
    def __init__(self, num, time=8):
        self.num = num
        self.time = time

    def epoch(self):
        self.time = 6 if self.time == 0 else self.time - 1

def epoch(fish):
    baby_fish = 0
    for f in fish:
        if f.time == 0:
            baby_fish += f.num
        f.epoch()
    if baby_fish > 0:
        fish.append(School(baby_fish, 8))

def solve(input, days):
    fish = [int(i) for i in input.split(",")]
    fish = [School(1, f) for f in fish]
    for day in range(0, days):
        epoch(fish)
    return sum([f.num for f in fish])

with open("./input.txt") as f:
    input = f.read()

class Test(unittest.TestCase):
    def test_solve_input(self):
        self.assertEqual(solve(input, 80), 350917)

    def test_solve_input(self):
        self.assertEqual(solve(input, 256), 1_592_918_715_629)

    def test_solve_sample_18(self):
        self.assertEqual(solve(sample, 18), 26)

    def test_solve_sample_80(self):
        self.assertEqual(solve(sample, 80), 5934)

    def test_solve_sample_256(self):
        self.assertEqual(solve(sample, 256), 26_984_457_539)
        pass

sample = "3,4,3,1,2"

unittest.main()
