from board import Board


def test_has_won():
    board = Board([[0,0,0,0,0] for i in range(5)])
    assert not board.has_won()
    board.marked_squares = [[1,1,1,1,1] for i in range(5)]
    assert board.has_won()
    board.marked_squares = [[1,0,0,0,0] for i in range(5)]
    assert board.has_won()


