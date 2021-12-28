from copy import deepcopy
import unittest

class Board:
    def __init__(self, rows):
        self.rows = rows
        self.winner = False

    def __repr__(self):
        return str(self.rows) + "\n\n"

    def mark(self, value):
        for row in self.rows:
            for cell in row:
                if (cell.value == value):
                    cell.marked = True

    def check_winner(self):
        winner = self.check_rows() or self.check_columns()
        if winner:
            self.winner = True
        return winner

    def check_rows(self):
        for row in self.rows:
            row = map(lambda cell: cell.marked, row)
            if all(row):
                return True
        return False

    def columns(self):
        return false

    def check_columns(self):
        for index in range(0, len(self.rows[0])):
            column = map(lambda row: row[index].marked, self.rows)
            if all(column):
                return True
        return False

class Cell:
    def __init__(self, value):
        self.value = value
        self.marked = False

    def __repr__(self):
        return self.value + ("m" if self.marked else "")

def mark_winners(boards):
    for board in boards:
        board.check_winner()

def sum_unmarked(board):
    sum = 0
    for row in board.rows:
        for cell in row:
            if not cell.marked:
                sum += int(cell.value)
    return sum

def check_winner(boards):
    for board in boards:
        if board.check_winner():
            return board
    return False

def mark_boards(draw, boards):
    for board in boards:
        board.mark(draw)

def create_board(instructions):
    rows = list(map(lambda r: list(map(Cell, r.strip().split())), instructions.strip().split('\n')))
    return Board(rows)

def parse_input(input):
    parts = input.split('\n\n')
    draws = parts[0].split(',')
    boards = list(map(create_board, parts[1:]))
    return (draws, boards)

def solve(input):
    [draws, boards] = parse_input(input)
    for draw in draws:
        mark_boards(draw, boards)
        winner = check_winner(boards)
        if winner:
            return sum_unmarked(winner) * int(draw)
    return (draws, boards)

def solve2(input):
    [draws, boards] = parse_input(input)
    for draw in draws:
        old_boards = deepcopy(boards)
        mark_boards(draw, boards)
        mark_winners(boards)
        losers = sum([0 if board.winner else 1 for board in boards])
        if losers == 0:
            board = [board for board in old_boards if not board.winner][0]
            return (sum_unmarked(board) - int(draw)) * int(draw)

    return (draws, boards)

with open("./input.txt") as f:
    input = f.read()

class Test(unittest.TestCase):
    def test_check_rows(self):
        rows = [[Cell("7"), Cell("7"), Cell("7"), Cell("7"), Cell("7")]]
        board = Board(rows)
        self.assertEqual(board.check_rows(), False)
        board.mark("7")
        self.assertEqual(board.check_rows(), True)

    def test_check_columns(self):
        rows = [[Cell("8"), Cell("7")], [Cell("8"), Cell("7")], [Cell("8"), Cell("7")], [Cell("8"), Cell("7")], [Cell("8"), Cell("7")]]
        board = Board(rows)
        self.assertEqual(board.check_columns(), False)
        board.mark("8")
        self.assertEqual(board.check_columns(), True)

    def test_solve_sample(self):
        self.assertEqual(solve(sample), 4512)

    def test_solve2_sample(self):
        self.assertEqual(solve2(sample), 1924)

    def test_solve_input(self):
        self.assertEqual(solve(input), 58412)

    def test_solve2_input(self):
        self.assertEqual(solve2(input), 10030)
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
