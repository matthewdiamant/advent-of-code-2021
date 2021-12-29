import unittest

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

with open("./input.txt") as f:
    input = f.read()

class Test(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(solve(input), 284)

    def test_sample(self):
        self.assertEqual(solve(sample), 26)

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

unittest.main()
