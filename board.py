import unittest as unit


class Board:
    def __init__(self):
        self.__board = [
            ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--"]]

        self.filledboard = [
            ["--", "--", "--", "--", "dr", "--", "dr", "--", "dr", "--", "--", "--"],
            ["--", "--", "--", "ma", "ma", "--", "--", "ma", "ma", "--", "--", "--"],
            ["--", "--", "--", "or", "--", "--", "or", "--", "--", "or", "--", "--"],
            ["--", "--", "--", "--", "or", "--", "--", "--", "or", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "kn", "--", "--", "--", "kn", "--", "--", "--", "--"],
            ["--", "--", "kn", "--", "--", "kn", "--", "--", "kn", "--", "--", "--"],
            ["--", "--", "--", "ar", "ar", "--", "--", "ar", "ar", "--", "--", "--"],
            ["--", "--", "--", "ca", "--", "ca", "--", "ca", "--", "--", "--", "--"]]

        self.__vert = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', 'f']
        self.__hor = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l']
        self.__whiteturn = True

    def get_board(self):
        return self.__board

    def get_filledboard(self):
        return self.filledboard

    def get_hor(self):
        return self.__hor

    def get_vert(self):
        return self.__vert

    def makemove(self, move, status):
        status[move.startrow][move.startcol] = '--'
        status[move.finishrow][move.finishcol] = move.moovingpiece
        move.movelog.append(move)
        self.__whiteturn = not self.__whiteturn

    def undomove(self, move, status):
        print("test")


class Testboard(unit.TestCase):
    def test_get_board(self):
        self.assertEqual(type(Board().get_board()), type([]))
        self.assertEqual(type(Board().get_filledboard()), type([]))

    def test_get_hor(self):
        self.assertEqual(type(Board().get_hor()), type([]))

    def test_get_ver(self):
        self.assertEqual(type(Board().get_vert()), type([]))

