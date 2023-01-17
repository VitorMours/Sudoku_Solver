from time import sleep
class Solver:
    """
    class Solver(object)
    | Create an object with the provided matrix, and allows
    | the usage of the methods inside the class.

    Parameters
    ----------
    | board: list of lists
        The sudoku board in format of matrix (list of lists).
    | block_width: int 
        width of the each division of the board
    | block_height: int
        height of the each division of the board
    |
    |
    |

    Returns
    -------
    |
    |
    
    
    """
    def __init__(self, board, block_width, block_height):
        self.validation = False
        self.board = board
        self.block_width = block_width
        self.block_height = block_height


    def visualization(self):
        for index, lines in enumerate(self.board):
            if (1 + index) % self.block_height == 0:
                print("-" * 60)
            for index, columns in enumerate(self.board[lines]):
                if (index + 1) % self.block_width == 0:
                    print(" | ")



    def empty(self):
        """"""
        for lines in range(len(self.board)):
            for columns in range(len(self.board[lines])):
                if self.board[lines][columns] == 0:
                    return lines, columns
        return None


    def solve(self):
        """"""
        find = self.empty()
        if not find:
            return True
        else:    
            lines, columns = find
            for option in range(1, self.size + 1):
                if self.validate(option, lines, columns):
                    self.board[lines][columns] = option
                    sleep(0.1)
                    self.show()
                    if self.solve():
                        return True

                self.board[lines][columns] = 0                    
        return False



        # Resolution - Doing
    def validate(self, option, lines, columns):
        """"""
        # Lines
        if option in self.board[lines]:
            return False                   

        # Columns
        for pos in range(self.size):
            if option == self.board[pos][columns]:
                return False

        # Box
        square = int(self.size ** 0.5)
        x_box = (columns // square) * square
        y_box = (lines // square) * square

        for x_elements in range(x_box, x_box + square):
            for y_elements in range(y_box, y_box + square):
                if option == self.board[y_elements][x_elements]:
                    return False
        # That number is possible
        return True


class Generator:
    """"""