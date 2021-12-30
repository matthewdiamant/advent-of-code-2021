import unittest

OPEN_CHARS = ["(", "[", "{", "<"]
CLOSE_CHARS = [")", "]", "}", ">"]

def corrupted(line):
    stack = []
    for char in line:
        if char in OPEN_CHARS:
            stack.append(char)
        else:
            if stack[-1] == OPEN_CHARS[CLOSE_CHARS.index(char)]:
                stack.pop()
            else:
                return char
    return False

def complete(line):
    stack = []
    for char in line:
        if char in OPEN_CHARS:
            stack.append(char)
        else:
            stack.pop()

    complete = [CLOSE_CHARS[OPEN_CHARS.index(char)] for char in stack]
    return list(reversed(complete))

def solve(input):
    lines = input.split("\n")
    POINTS = { ")": 3, "]": 57, "}": 1197, ">": 25137 }
    corrupted_lines = [corrupted(line) for line in lines]
    points = [POINTS[line] for line in corrupted_lines if line]
    return sum(points)

def score(complete):
    POINTS = { ")": 1, "]": 2, "}": 3, ">": 4 }
    sum = 0
    for char in complete:
        sum *= 5
        sum += POINTS[char]
    return sum

def solve2(input):
    lines = input.split("\n")
    completable = [line for line in lines if not corrupted(line)]
    scores = sorted([score(complete(line)) for line in completable])
    middle = scores[len(scores) // 2]
    return middle

with open("./input.txt") as f:
    input = f.read()

class Test(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(solve(sample), 26397)

    def test_solve(self):
        self.assertEqual(solve(input), 311949)

    def test_sample2(self):
        self.assertEqual(solve2(sample), 288957)

    def test_solve2(self):
        self.assertEqual(solve2(input), 3042730309)

sample = """[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]"""

unittest.main()
