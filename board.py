import numpy as np

SCORE_WIN  =  1
SCORE_LOSE = -1
SCORE_TIE  =  0

def opposite(player):
    if player is 'X': return 'O'
    return 'X'

class Board():
    def __init__(self, board=[ ['', '', ''],
                               ['', '', ''],
                               ['', '', ''] ]):
        self.board = np.asarray(board)
        self.score = 0

    def get_score(self, player, maxdepth=2):
        maxdepth_new = maxdepth - 1
        for row in self.board:
            if np.all(row == player):
                return SCORE_WIN
        for row in np.transpose(self.board):
            if np.all(row == player):
                return SCORE_WIN
        if np.all( np.diagonal(self.board) == player):
            return SCORE_WIN
        if np.all( np.diagonal(np.fliplr(self.board)) == player ):
            return SCORE_WIN
        if maxdepth_new == 0:
            return SCORE_TIE
        if self.get_score(opposite(player), maxdepth_new):
            return SCORE_LOSE


test_board = [ ['X', 'X', 'X' ],
               ['', 'O', 'O'],
               ['', 'O', 'X'] ]

other_board = [ ['X', 'O', 'X'],
                ['', 'X', ''],
                ['O', 'O', 'O']]

board = Board(test_board)
print(board.get_score('X'))

board2 = Board(other_board)
print(board2.get_score('X'))
