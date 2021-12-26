import unittest

class Board:
    def __init__(self, rows):
        self.rows = rows

    def mark(self, value):
        for row in self.rows:
            for cell in row:
                if (cell.value == value):
                    cell.marked = True

    def check_winner(self):
        return self.check_rows() or self.check_columns()

    def check_rows(self):
        return any([all(map(lambda cell: cell.marked, row)) for row in rows])

    def columns(self):

    def check_columns(self):
        columns = []
        for idx from range(len(self.rows)):
            cells = map(lambda row: row[idx], rows)
        return all(map(lambda cell: cell.marked, cells))

class Cell:
    def __init__(self, value):
        self.value = value
        self.marked = False

    def __repr__(self):
        return self.value

def create_board(instructions):
    return Board(map(lambda r: map(Cell, r.strip().split()), instructions.split('\n')))

def parse_input(input):
    parts = input.split('\n\n')
    draws = parts[0].split(',')
    boards = map(create_board, parts[1:])
    return (draws, boards)

def solve(input):
    [draws, boards] = parse_input(input)
    return (draws, boards)

with open("./input.txt") as f:
    input = f.read()

class Test(unittest.TestCase):
    def test_solve_sample(self):
        self.assertEqual(solve(sample), None)

    def test_solve_input(self):
        # self.assertEqual(solve(input), None)
        pass

sample = """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7"""

unittest.main()
