class Solver:
    def __init__(self, board, size):
        self.board = board
        self.size = size
        
        
    def show(self):
        for lines in range(len(self.board)):
            if lines % self.size == 0 or lines == 0:
                print('\n' + '-' * 25, end='')
            print('')
            for columns in range(len(self.board[lines])):
                if columns % self.size == 0:
                    print('| ', end='')
                if columns == (self.size ** 2) - 1:
                    print(f'{self.board[lines][columns]} |', end='')
                else:
                    print(f'{self.board[lines][columns]}', end=' ')
        print('\n' + '-' * 25)
                