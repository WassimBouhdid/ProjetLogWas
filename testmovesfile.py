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