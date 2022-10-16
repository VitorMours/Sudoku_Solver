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
                print(f'Analisando opções do elemento: [{lines},{columns}]')
                validation(board, lines, columns)
            else:
                continue 
            
           
def validation(board,lines,col):
    possis = []
    for pos in range(9):
        # Linhas
        possis.append(board[lines][pos])
        print(f'Adicionando o elemento [{lines},{pos}] nas impossibilidades: {board[lines][pos]}')
    print('-' * 58)
        # Colunas
    for pos in range(9):
        possis.append(board[pos][col])
        print(f'Adicionando o elemento [{pos},{col}] nas impossibilidades: {board[pos][col]}')
    
    print(set(sorted(possis)))
    print('\n')
    # 'Caixa'
            
            
        
# Exibição ao usuário
show(board)
empty(board)
filling(board)
