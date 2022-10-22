from time import sleep
class Solver:
    def __init__(self, board, size):
        self.validation = False
        self.board = board
        self.size = size
        
    # Visualization - OK   
    def show(self):
        for lines in range(len(self.board)):
            if lines % self.size == 0 or lines == 0:
                print('\n' + '-' * 25, end='')
            print('')
            for columns in range(len(self.board[lines])):
                if columns % self.size == 0:
                    print('| ', end='')
                
                if self.board[lines][columns] == 0:
                    if columns == (self.size ** 2) - 1:
                        print(f' |', end='')
                    else:
                        print(f'  ', end='')
                    
                else:    
                    if columns == (self.size ** 2) - 1:
                        print(f'{self.board[lines][columns]} |', end='')
                    else:
                        print(f'{self.board[lines][columns]}', end=' ')
        print('\n' + '-' * 25)
    
    
    
    
        # Resolution - Doing
    def validate(self, option, lines, columns):
        # Lines
        if option in self.board[lines]:
            return False                   
        
        # Columns
        for pos in range(9):
            if option == self.board[pos][columns]:
                return False
        
        # Box
        x_box = (columns // 3) * 3
        y_box = (lines // 3) * 3
        for x_elements in range(x_box, x_box + 3):
            for y_elements in range(y_box, y_box + 3):
                if option == self.board[y_elements][x_elements]:
                    return False
        # That number is possible
        return True

    
    
    # Solution - 
    def solve(self):
        for lines in range(len(self.board)):
            for columns in range(len(self.board[lines])):
                if self.board[lines][columns] == 0:
                    for option in range(1,10):
                        results = self.validate(option, lines, columns)
                        if results:
                            self.board[lines][columns] = option
                            self.show()
                            #sleep(0.5)
        print('-=' * 30)
        
        