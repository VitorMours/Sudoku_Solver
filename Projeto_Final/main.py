from solver import Solver
from time import sleep
board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]
sudoku_9 = Solver(board,9)
sudoku_9.show()
sudoku_9.solve()
sudoku_9.show()
 
sleep(2)

print('\nAgora resolvendo sudoku 4x4')
board_4 = [ [0, 4, 0, 1],
            [3, 0, 0, 0],
            [0, 0, 0, 4],
            [0, 0, 0, 0]]

sudoku_4 = Solver(board_4,4)
sudoku_4.show()
sudoku_4.solve()
sudoku_4.show()