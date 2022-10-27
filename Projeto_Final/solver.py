from time import sleep
class Solver:
 
    #TODO fazer todas as partes do código ficarem em função do tamanho do jogo e do tipo
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
                
                if columns == (self.size ** 2) - 1:
                    print(f'{self.board[lines][columns]} |', end='')
                else:
                    print(f'{self.board[lines][columns]}', end=' ')
        print('\n' + '-' * 25)
    
    def empty(self):
        for lines in range(len(self.board)):
            for columns in range(len(self.board[lines])):
                if self.board[lines][columns] == 0:
                    return lines, columns
        return None
    
    
    def solve(self):
        find = self.empty()
        if not find:
            return True
        else:    
            lines, columns = find
            for option in range(1, 10):
                if self.validate(option, lines, columns):
                    self.board[lines][columns] = option
                    sleep(0.5)
                    self.show()
                    if self.solve():
                        return True

                self.board[lines][columns] = 0                    
        return False
    
    
    
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


        
        