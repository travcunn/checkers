import json

from textcolors import colors


class Checkers(object):
    """ The checkers game. """

    colors = {'black': 0,
               'red': 1}

    def __init__(self, size=8):
        """
        Args:
            size (int): The size of the board
        """
        self.__board = []
        self.__size = size

        # starts with the red player
        self.__turn = colors['red']

        self.reset()

    @property
    def turn(self):
        """ Returns the player whose turn it is. """
        return self.__turn

    @property
    def board(self):
        """ Returns the board information. """
        return self.__board

    def move(self, src, dest):
        """ Moves the src game piece to the dest.

        :param src: The piece to move
        :param dest: The piece destination
        """
        pass

    def reset(self):
        # populate the board with None
        self.__board = [[None for y in range(self.__size)] \
                        for x in range(self.__size)]

        # populate the board with game pieces
        for y in range(len(self.__board)):
            for x in range(len(self.__board)):
                # generate the red team
                if x < 3:
                    if (x % 2 == 0) and (y % 2 == 1):
                        self.__board[x][y] = Piece(self.colors['red'])
                    if (x % 2 == 1) and (y % 2 == 0):
                        self.__board[x][y] = Piece(self.colors['red'])
                 # generate the black team
                if x > len(self.__board) - 4:
                    if (x % 2 == 0) and (y % 2 == 1):
                        self.__board[x][y] = Piece(self.colors['black'])
                    if (x % 2 == 1) and (y % 2 == 0):
                        self.__board[x][y] = Piece(self.colors['black'])

    def display(self):
        new_line = "\n"
        output = ""

        output = output + "|"
        for top_border in range(len(self.__board) * 1):
            output = output + str("===")
        output = output + "|" + new_line

        for x in range(len(self.__board)):
            output = output + "|"
            for y in range(len(self.__board)):
                # generate red squares
                if (x % 2 == 0) and (y % 2 == 1):
                    output = output + colors['on_red']
                if (x % 2 == 1) and (y % 2 == 0):
                    output = output + colors['on_red']
                # X, O, or blank
                space = self.__board[x][y]
                if space is not None:
                    if space.color == self.colors['red']:
                        output = output + " O "
                    elif space.color == self.colors['black']:
                        output = output + " X "
                else:
                    output = output + "   "
                output = output + colors['default']
            output = output + "|" + new_line

        output = output + "|"
        for top_border in range(len(self.__board) * 1):
            output = output + str("===")
        output = output + "|" + new_line

        print(output)


class Piece(object):
    """ Represents a game piece given a color. """
    def __init__(self, color):
        """
        Args:
            color (int): The color of the game piece
        """
        self.__color = color
        self.__is_king = False

        if self.__color is Checkers.colors['red']:
            self.__possible_moves = [(1, 1), (1, -1)]
        else:
            self.__possible_moves = [(-1, -1), (-1, 1)]

    @property
    def color(self):
        return self.__color

    @property
    def is_king(self):
        return self.__is_king

    @property
    def possible_moves(self):
        return self.__possible_moves

    def king(self):
        """ Sets the piece to a king. """
        self.__is_king = True

        # expand the possible moves
        z = [1, -1]
        self.__possible_moves = [(x, y) for x in z for y in z]

    def __repr__(self):
        return "<GamePiece: %s>" % (self.color)
