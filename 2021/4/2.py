from board import Board

with open('input') as f:
    lines = f.read().strip().split('\n')

drawn_numbers = [int(x) for x in lines[0].split(',')]


def parse_boardline(l):
    r = []
    r.append(int(l[:2].strip()))
    r.append(int(l[3:5].strip()))
    r.append(int(l[6:8].strip()))
    r.append(int(l[9:11].strip()))
    r.append(int(l[12:].strip()))
    return r
boards = []
for i in range(1, len(lines), 6):
    board = []
    for j in range(1,6):
        board.append(parse_boardline(lines[i+j]))
    boards.append(Board(board))
def run_bingo(boards):
    k=0
    won_boards = [0]*len(boards)
    last_won = None
    while sum(won_boards) < len(boards):
        num = drawn_numbers[k]
        for i,board in enumerate(boards):
            board.mark_number(num)
            if board.has_won():
                if not won_boards[i]:
                    won_boards[i] = 1
                    last_won = i
        k+=1
    return k-1, boards[last_won]
(k, loser) = run_bingo(boards)
print(loser.sum_unmarked()*drawn_numbers[k])

