import unittest

def determine_values(key):
    values = {}
    one_key = [digit for digit in key if len(digit) == 2][0]
    seven_key = [digit for digit in key if len(digit) == 3][0]
    four_key = [digit for digit in key if len(digit) == 4][0]
    eight_key = [digit for digit in key if len(digit) == 7][0]
    two_three_five = [digit for digit in key if len(digit) == 5]
    zero_six_nine = [digit for digit in key if len(digit) == 6]
    three_key = [digit for digit in two_three_five if one_key[0] in digit and one_key[1] in digit][0]
    nine_key = [digit for digit in zero_six_nine if all([seg in digit for seg in three_key])][0]
    five_key = [digit for digit in two_three_five if digit != three_key and all([seg in nine_key for seg in digit])][0]
    two_key = [digit for digit in two_three_five if digit != three_key and digit != five_key][0]
    six_key = [digit for digit in zero_six_nine if digit != nine_key and all([seg in digit for seg in five_key])][0]
    zero_key = [digit for digit in zero_six_nine if digit != six_key and digit != nine_key][0]
    values[zero_key] = '0'
    values[one_key] = '1'
    values[two_key] = '2'
    values[three_key] = '3'
    values[four_key] = '4'
    values[five_key] = '5'
    values[six_key] = '6'
    values[seven_key] = '7'
    values[eight_key] = '8'
    values[nine_key] = '9'
    return values

def count_unique(lines):
    unique = [[digit for digit in line[1] if len(digit) in [2, 3, 4, 7]] for line in lines]
    return sum([len(line) for line in unique])

def parse_input(input):
    return [
        [digits.split(" ") for digits in line.strip().split(" | ")]
        for line in input.strip().split("\n")
    ]

def solve(input):
    lines = parse_input(input)
    return count_unique(lines)

def solve2(input):
    lines = parse_input(input)
    nums = []
    for line in lines:
        values = determine_values(line[0])
        num = ""
        for digit in line[1]:
            for value in values:
                if len(digit) == len(value) and all([seg in value for seg in digit]):
                    num += values[value]
        nums.append(num)
    return sum([int(num) for num in nums])

with open("./input.txt") as f:
    input = f.read()

class Test(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(solve(input), 284)

    def test_sample(self):
        self.assertEqual(solve(sample), 26)

    def test_solve2(self):
        self.assertEqual(solve2(input), 973499)

    def test_solve2_sample(self):
        self.assertEqual(solve2(sample), 61229)

    def test_solve3_sample2(self):
        self.assertEqual(solve2(sample2), 5353)

sample = """be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce"""

sample2 = """acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf"""

unittest.main()
