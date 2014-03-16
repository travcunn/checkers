from colorama import init, Back

# enable colorama
init()


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

        self.reset()

    @property
    def board(self):
        """ Returns the board information. """
        return self.__board

    def move(self, src, dest):
        """ Moves the src game piece to the dest.

        :param src: The piece to move
        :param dest: The piece destination
        """
        x_src, y_src = src
        x_dest, y_dest = dest

        piece = self.__board[y_src][x_src]
        if piece is None:
            raise KeyError("There is no game piece at this location.")

        dest_piece = self.__board[y_dest][x_dest]
        if dest_piece is None:  # check that nothing is in the spot
            move = x_dest - x_src, y_dest - y_src
            if move in piece.possible_moves:
                self.__board[y_src][x_src] = None
                self.__board[y_dest][x_dest] = piece
            else:
                raise MoveError("That move is invalid.")
        else:
            raise MoveError("There is already a piece in this spot.")

    def reset(self):
        # populate the board with None
        self.__board = [[None for y in range(self.__size)]
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

    def display(self):  # pragma: no cover
        new_line = "\n"
        output = ""

        output = output + new_line + "|"
        for top_border in range(len(self.__board) * 1):
            output = output + str("===")
        output = output + "|" + new_line

        for x in range(len(self.__board)):
            output = output + "|"
            for y in range(len(self.__board)):
                # generate red squares
                if (x % 2 == 0) and (y % 2 == 1):
                    output = output + Back.RED
                if (x % 2 == 1) and (y % 2 == 0):
                    output = output + Back.RED
                # X, O, or blank
                space = self.__board[x][y]
                if space is not None:
                    if space.color == self.colors['red']:
                        output = output + " O "
                    elif space.color == self.colors['black']:
                        output = output + " X "
                else:
                    output = output + "   "
                output = output + Back.RESET
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
            self.__possible_moves = [(1, 1), (-1, 1)]
        else:
            self.__possible_moves = [(-1, -1), (1, -1)]

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


class MoveError(Exception):
    pass
