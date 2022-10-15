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

#def visualization():
#    pass


def show(matrix):
    print('\n')
    print(f'{" Mostrando sudoku ":=^28}')

    # Exibindo o jogo ao usuário    
    for lines in range(len(matrix)):
        if lines % 3 == 0 and lines != 0:
            print('-' * 28)
        for columns in range(len(matrix)):
            if columns % 3 == 0 and columns != 0:
                print('|', end='') 
            if columns == 8:
                print(f' {matrix[lines][columns]}')
            else:     
                print(f' {matrix[lines][columns]}', end = ' ')
    print('-' * 28)
    
            
def empty(matrix):
    print('\nPosição da matriz com valores vazios:') 
    for lines in range(len(matrix)):
        print(f'\n{lines}ª linha: ')
        for columns in range(len(matrix[0])):
            if matrix[lines][columns] == 0:
                print(f'{lines},{columns}')
            else:
                continue 

def filling(matrix):
    for lines in range(len(matrix)):
        for columns in range(len(matrix[0])):
            if matrix[lines][columns] == 0:
                print(f'\nTestando elemento [{lines},{columns}] com o valor: ',end='')
                for numbers in range(1,10):
                    if numbers in matrix[lines]:
                        for range()
                        continue
                    else:
                        matrix[lines][columns] = numbers
                        print(f'{numbers}',end='')
    show(board)
            
           
def validating(board):
    pass            
# Exibição ao usuário
show(board)
empty(board)
filling(board)
