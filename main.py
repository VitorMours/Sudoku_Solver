
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


def mostrar(matriz):
    for lines in range(len(matriz)):
        print('')
        for columns in range(len(matriz[lines])):
            try:
                print(matriz[lines][columns], end=' ')
            except matriz[lines][columns] is None:
                continue


def possibilidades(matriz):
    possibilities = []
    for lines in range(len(matriz)):
        options = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for columns in matriz[lines]:
            if columns in options:
                options.remove(columns)
        possibilities.append(options)

    for lines_options in possibilities:
        return lines_options


def validar(matriz):
    for lines in matriz:
        for columns in lines:
            x0, y0 = 0,0







print(mostrar(board))
print('-' * 80)
print(possibilidades(board))

