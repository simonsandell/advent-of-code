from operator import add
class Board:
    def __init__(self, board):
        self.board_numbers = board
        self.marked_squares = [[0,0,0,0,0] for i in range(5)]

    def has_won(self):
        v = [0] * 5 
        for i in range(5):
            if sum(self.marked_squares[i]) == 5:
                return True
            v = list(map(add, v, self.marked_squares[i]))
        if 5 in v:
            return True
        return False

    def mark_number(self, num):
        for i in range(5):
            for j in range(5):
                if self.board_numbers[i][j] == num:
                    self.marked_squares[i][j] = 1
    def sum_unmarked(self):
        s = 0
        for i in range(5):
            for j in range(5):
                if self.marked_squares[i][j] == 0:
                    s += self.board_numbers[i][j]
        return s
