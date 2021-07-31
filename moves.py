from board import Board
import unittest as unit
B = Board()

class Moves:
    rankstorows = {"a": 11, "b": 10, "c": 9, "d": 8, "e": 7, "f": 6,
                   "g": 5, "h": 4, "i": 3, "j": 2, "k": 1, "l": 0}
    rowstoranks = {v: k for k, v in rankstorows.items()}
    filestocols = {"1": 0, "2": 1, "3": 2, "4": 3, "5": 4, "6": 5,
                   "7": 6, "8": 7, "9": 8, "10": 9, "11": 10, '12': 11}
    colstofiles = {v: k for k, v in filestocols.items()}

    def __init__(self, start, finish, board):
        self.startrow = start[1]
        self.startcol = start[0]
        self.finishrow = finish[1]
        self.finishcol = finish[0]
        self.moovingpiece = board[self.startrow][self.startcol]
        self.capturedpiece = board[self.finishrow][self.finishcol]
        self.movelog = []

    def get_rankfile(self, r, c):
        return self.colstofiles[c] + self.rowstoranks[r]

    def getpositionnotation(self):
        return self.get_rankfile(self.startrow, self.startcol) + self.get_rankfile(self.finishrow,
                                                                                   self.finishcol)





class Testmove(unit.TestCase):
    def test_get_rankfiles(self):
        self.assertEqual(type(Moves((2, 2), (4, 6), Board().get_filledboard()).get_rankfile(4, 6)), type('a'))

    def test_get_position_notation(self):
        self.assertEqual(type(Moves((2, 2), (4, 6), Board().get_filledboard()).getpositionnotation()), type('a'))
