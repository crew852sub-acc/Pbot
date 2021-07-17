"""
오목(Gomoku) 게임 구현

작성자: 김종하
"""

from enum import Enum

from GameBase import gameBase

# in-game feature

class Turn(Enum):
    BLACK = 0
    WHITE = 1

class GameGomoku(gameBase.Game):
    COLUMN = 15
    ROW = 15
    board = [[0 for i in range(COLUMN)] for j in range(ROW)]

    # game
    def __init__(self):        
        return

    def placement(self):    

        return

    def showResult(self):

        return

    def __checkEnd(self):
        result = False

        return result