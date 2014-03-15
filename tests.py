import unittest

from game import Checkers, Piece


class CheckersTest(unittest.TestCase):
    def test_board_generation(self):
        c = Checkers(8)

        c.display()

        # make sure there are 12 red pieces on the board
        all_red = [[x.color for x in y if x is not None and x.color is \
                    Checkers.colors['red']] for y in c.board]
        red_count = 0
        for y in all_red:
            red_count += len(y)
        self.assertTrue(red_count is 12)

        # make sure there are 12 black pieces on the board
        all_black = [[x.color for x in y if x is not None and x.color is \
                      Checkers.colors['black']] for y in c.board]
        black_count = 0
        for y in all_black:
            black_count += len(y)
        self.assertTrue(black_count is 12)


class PieceTest(unittest.TestCase):
    def test_attributes(self):
        p = Piece(Checkers.colors['red'])
        # test colors
        self.assertTrue(p.color == Checkers.colors['red'])

    def test_repr(self):
        p = Piece(Checkers.colors['red'])
        expected = "<GamePiece: " + str(Checkers.colors['red']) + ">"
        self.assertTrue(repr(p) == expected)

    def test_possible_moves_and_king(self):
        p = Piece(Checkers.colors['red'])
        self.assertTrue(p.is_king is False)
        self.assertTrue(p.possible_moves == [(1, 1), (1, -1)])

        p.king()
        self.assertTrue(p.is_king)
        all_moves = [(1, 1), (1, -1), (-1, 1), (-1, -1)]

        self.assertTrue(p.possible_moves == all_moves)

        p = Piece(Checkers.colors['black'])
        self.assertTrue(p.is_king is False)
        self.assertTrue(p.possible_moves == [(-1, -1), (-1, 1)])



if __name__ == '__main__':
    unittest.main()
