import unittest

def gamma_oxygen(ratio):
    return "1" if ratio >= 0.5 else "0"

def epsilon_co2(ratio):
    return "0" if ratio >= 0.5 else "1"

def solve_part_1(input):
    reports = input.split()
    rates = {}
    for position in range(len(reports[0])):
        rates[position] = sum([int(report[position]) for report in reports])
    gamma = "".join([gamma_oxygen(rate / len(reports)) for rate in rates.values()])
    epsilon = "".join([epsilon_co2(rate / len(reports)) for rate in rates.values()])
    return int(gamma, 2) * int(epsilon, 2)

def find(reports, filter):
    for position in range(len(reports[0])):
        rate = sum([int(report[position]) for report in reports])
        reports = [r for r in reports if r[position] == filter(rate / len(reports))]
        if (len(reports) == 1):
            return reports[0]

def solve_part_2(input):
    reports = input.split()
    oxygen = find(reports, gamma_oxygen)
    co2 = find(reports, epsilon_co2)
    return int(oxygen, 2) * int(co2, 2)

with open("./input.txt") as f:
    input = f.read()

class Test(unittest.TestCase):
    def test_solve_part_1_input(self):
        self.assertEqual(solve_part_1(input), 4160394)

    def test_solve_part_1_sample(self):
        self.assertEqual(solve_part_1(sample), 198)

    def test_solve_part_2_input(self):
        self.assertEqual(solve_part_2(input), 4125600)

    def test_solve_part_2_sample(self):
        self.assertEqual(solve_part_2(sample), 230)

sample = """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010"""

unittest.main()
