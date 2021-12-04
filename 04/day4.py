from collections import Counter
from functools import reduce
from itertools import groupby

class Board:
    def is_bingo(self, series):
        bingo = sum([x[0] for x in series]) == self.row
        if bingo:
            board_values = [int(number) for number in [item for sublist in self._raw_board for item in sublist] if number not in self.draws]
            return sum(board_values)
        return 0

    def get_diagonals(self):
        return [self.positions[y][y] for y in range(self.row)] , [self.positions[self.row - y - 1][self.row - y - 1] for y in range(self.row)]

    def update(self, number):
        self.draws.append(number)
        for y, row in enumerate(self._raw_board):
            if number in row:
                x = row.index(number)
                self.positions[y][x] = (1, number)

    def has_winner(self, number):
        # diagonal_left, diagonal_right = self.get_diagonals()
        verticals = [[self.positions[y][x] for y in range(self.row)] for x in range(self.col)]
        horizontals = [[self.positions[y][x] for x in range(self.col)] for y in range(self.row)]
        winner = [series for series in [*verticals, *horizontals] if self.is_bingo(series) > 0]
        if (len(winner) > 0):
            return self.is_bingo(winner[0]) * int(number)
        return False

    def __init__(self, raw_board):
        self.draws = []
        self.row = len(raw_board)
        self.col = len(raw_board[0].split())
        self._raw_board = [row.split() for row in raw_board]
        self.positions =  [[(0, 0) for i in range(len(raw_board[0].split()))] for j in range(len(raw_board))]

def find_bingo_last_winner(input):
    command = input[0].split(',')
    boards = [Board(list(group)) for k, group in groupby(input[2:], lambda x: x == "") if not k]
    n_boards = len(boards)
    winners = {}

    for draw in command:
        if len(winners.keys()) == n_boards:
            return list(winners.values())[-1]
        for i, board in enumerate(boards):
            board.update(draw)
            winner = board.has_winner(draw)
            if winner:
                winners[i] = winner
    return winners[-1]

def find_bingo_winner(input):
    command = input[0].split(',')
    boards = [Board(list(group)) for k, group in groupby(input[2:], lambda x: x == "") if not k]

    for draw in command:
        for board in boards:
            board.update(draw)
            winner = board.has_winner(draw)
            if winner:
                return winner

if __name__ == "__main__":
    with open('part1.txt') as f:
        input = f.read().splitlines()
        ans = find_bingo_winner(input)
        print(f'Part 1: {ans}')

    with open('part2.txt') as f:
        input = f.read().splitlines()
        ans = find_bingo_last_winner(input)
        print(f'Part 2: {ans}')
