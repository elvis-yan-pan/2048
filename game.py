"""
2048 Game
Author: Elvis Pan
Email: ypan2@andrew.cmu.edu
"""
import random


def merge(temp):
    res = []
    score = 0
    for i in range(len(temp)):
        if temp[i] is None:
            pass
        elif i < len(temp) - 1 and temp[i + 1] == temp[i]:
            res.append(temp[i] * 2)
            score += temp[i] * 2
            temp[i + 1] = None
        else:
            res.append(temp[i])
    res.extend([0] * (4 - len(res)))
    return res, score


class Game:
    def __init__(self):
        self.board = [[0 for i in range(4)] for j in range(4)]
        self.score = 0
        self.status = True

    def start_game(self):
        self.add_random()
        self.add_random()

    def add_random(self, max_num=2):
        spots = []
        for i in range(4):
            for j in range(4):
                if self.board[i][j] == 0:
                    spots.append((i, j))
        if len(spots) == 0:
            self.game_over()
            return
        seed = random.randint(0, len(spots) - 1)
        coord = spots[seed]
        self.board[coord[0]][coord[1]] = 2

    def next(self, direction):  # d = 'u', 'd', 'l', 'r'
        # TODO: detect whether the move is valid
        assert self.status
        for i in range(4):
            temp = []
            if direction == 'u':
                for j in range(4):
                    if self.board[j][i] != 0:
                        temp.append(self.board[j][i])
                res, score = merge(temp)
                self.score += score
                for j in range(4):
                    self.board[j][i] = res[j]
            elif direction == 'd':
                for j in range(4):
                    if self.board[3 - j][i] != 0:
                        temp.append(self.board[3 - j][i])
                res, score = merge(temp)
                self.score += score
                for j in range(4):
                    self.board[3 - j][i] = res[j]
            elif direction == 'l':
                for j in range(4):
                    if self.board[i][j] != 0:
                        temp.append(self.board[i][j])
                res, score = merge(temp)
                self.score += score
                for j in range(4):
                    self.board[i][j] = res[j]
            else:
                assert direction == 'r'
                for j in range(4):
                    if self.board[i][3 - j] != 0:
                        temp.append(self.board[i][3 - j])
                res, score = merge(temp)
                self.score += score
                for j in range(4):
                    self.board[i][3 - j] = res[j]
        self.add_random()

    def game_over(self):
        # TODO: force the game to stop
        self.status = False


if __name__ == "__main__":
    print("Test Cases")
    """print(merge([2,2,4,4]))
    print(merge([2,4,4,2]))
    print(merge([2,2,2,4]))
    print(merge([2,4,4,4]))
    print(merge([2,2]))
    print(merge([2,2,2]))
    G = Game()
    G.board = [[2,2,2,2],[2,4,2,4],[2,4,0,0],[4,2,2,4]]
    G.next('d')
    print(G.board)
    G.board = [[2,0,2,0],[0,2,2,2],[4,4,4,4],[0,2,0,0]]
    G.next('r')
    print(G.board)"""
