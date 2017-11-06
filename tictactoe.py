from board import Board, opposite
import numpy as np
import time
import timeit

INFINITE = 10**10
expansions = 0
fn = open("results.txt", "w")

class TicTacToe():
    def __init__(self, player='X'):
        self.board = Board(player)
        self.player = player
        self.expansions = 0

    def start(self, player, function, x, y):
        score = self.board.get_score()
        depth = 9
        while score is None:
            print(self.board.board)
            x_player_1 = x
            y_player_1 = y
            self.board.board[x_player_1, y_player_1] = player

            start = timeit.default_timer()
            children = self.board.expand('O')
            for child in children:
                child.score = function(child, 9, 'X', 'O', -INFINITE, INFINITE)
                self.expansions += 1
                print(child.score)
            stop = timeit.default_timer()
            print("RunTime: " + str(stop - start))
            fn.write(str(x) + "," + str(y) + "\t" + str(self.expansions))
            fn.write("Runtime: " + str(stop-start))
            fn.write("\n")
            print(self.expansions)
            self.expansions = 0
            if children:
                max_board = max(children, key = lambda x: x.score)
                best_choices = list()
                print("max score " + str ( max_board.score ))
                for child in children:
                    if child.score == max_board.score:
                        best_choices.append(child)
                choice = np.random.randint(0, len(best_choices))
                self.board = best_choices[choice]
                print("Best choice random score " + str(best_choices[choice].score))
                depth -= 1
            score = self.board.get_score()
            self.player = opposite(self.player)
            return
        print(score, self.expansions)
        print(self.board.board)

    def minimax(self, board, depth, max_, min_, alpha, beta):
        if board.get_score() is not None or depth is 0:
            score = board.get_score()
            return score
        elif board.player is min_:
            util = INFINITE
            for child in board.expand(max_):
                self.expansions += 1
                util = min(util, self.minimax(child, depth-1, max_, min_, alpha, beta))
            return util
        else:
            util = -INFINITE
            for child in board.expand(min_):
                self.expansions += 1
                util = max(util, self.minimax(child, depth-1, max_, min_, alpha, beta))
            return util

    def alpha_beta(self, board, depth, max_, min_, alpha, beta):
        if board.get_score() is not None or depth is 0:
            score = board.get_score()
            return score
        elif board.player is min_:
            util = INFINITE
            for child in board.expand(max_):
                self.expansions += 1
                util = min(util, self.alpha_beta(child, depth-1, max_, min_, alpha, beta))
                beta = max(alpha, util)
                if beta <= alpha:
                    break
            return util
        else:
            util = -INFINITE
            for child in board.expand(min_):
                self.expansions += 1
                util = max(util, self.alpha_beta(child, depth-1, max_, min_, alpha, beta))
                alpha = min(beta, util)
                if beta <= alpha:
                    break
            return util

if __name__ == '__main__':
    for i in range(3):
        for j in range(3):
            game = TicTacToe()
            game.start('X', game.minimax, i, j)

    for i in range(3):
        for j in range(3):
            game = TicTacToe()
            game.start('X', game.alpha_beta, i, j)

    fn.close()
