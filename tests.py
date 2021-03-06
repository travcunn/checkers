import unittest

from checkers import Checkers, Piece, MoveError


class CheckersTest(unittest.TestCase):
    def test_board_generation(self):
        c = Checkers(8)

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

    def test_possible_moves_and_king(self):
        p = Piece(Checkers.colors['red'])
        self.assertTrue(p.is_king is False)
        self.assertTrue(p.possible_moves == [(1, 1), (-1, 1)])

        p.king()
        self.assertTrue(p.is_king)
        all_moves = [(1, 1), (1, -1), (-1, 1), (-1, -1)]

        self.assertTrue(p.possible_moves == all_moves)

        p = Piece(Checkers.colors['black'])
        self.assertTrue(p.is_king is False)
        self.assertTrue(p.possible_moves == [(-1, -1), (1, -1)])

    def test_move(self):
        c = Checkers()

        # COMMENTS ARE FROM THE PLAYER'S PERSPECTIVE

        # move red forward left
        self.assertTrue(c.board[3][2] is None)
        c.move(src=(1, 2), dest=(2, 3))
        self.assertTrue(c.board[3][2] is not None)

        # move red forward right
        self.assertTrue(c.board[4][1] is None)
        c.move(src=(2, 3), dest=(1, 4))
        self.assertTrue(c.board[4][1] is not None)

        # try moving red where an enemy is
        self.assertTrue(c.board[5][0].color is Checkers.colors['black'])
        with self.assertRaises(MoveError):
            c.move(src=(1, 4), dest=(0, 5))
        self.assertTrue(c.board[5][0].color is Checkers.colors['black'])

        # try moving red backwards as a regular piece
        self.assertTrue(c.board[3][2] is None)
        with self.assertRaises(MoveError):
            c.move(src=(1, 4), dest=(2, 3))

        # try moving a piece that doesn't exist
        self.assertTrue(c.board[3][1] is None)
        with self.assertRaises(KeyError):
            c.move(src=(1, 3), dest=(2, 2))

    def test_single_jump(self):
        c = Checkers()

        # move a red piece in a position where black can jump
        c.move(src=(1, 2), dest=(2, 3))
        c.move(src=(2, 3), dest=(3, 4))

        # make sure the destination is empty
        self.assertTrue(c.board[3][4] is None)
        # jump a black piece over the red piece
        c.move(src=(2, 5), dest=(4, 3))
        # make sure the piece is at the destination
        self.assertTrue(c.board[3][4].color is Checkers.colors['black'])
        # make sure the jumped piece is removed from the board
        self.assertTrue(c.board[4][3] is None)

    def test_invalid_jump(self):
        c = Checkers()

        # try jumping over the same colored piece
        with self.assertRaises(MoveError):
            c.move(src=(2, 1), dest=(0, 3))


if __name__ == '__main__':
    unittest.main()
