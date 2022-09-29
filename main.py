#import Show
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

# TODO transformar a função em orientação objeto no outro documento e
def mostrar(matriz):
    for lines in range(len(matriz)):
        print('')
        for columns in range(len(matriz[lines])):
            try:
                print(matriz[lines][columns], end=' ')
            except matriz[lines][columns] is None:
                continue


def show(*args):
    linha = 1
    for elements in range(len(args)):
        print(f'Mostrando os elementos da {linha}ª linha: ')
        for sub_elements in range(len(args[elements])):
            print(f'{args[elements][sub_elements]}')
        linha += 1

# TODO Refatorar o código para evitar repettição de estruturas e laços desnecessários.
def validar(matriz):
    x_options = []
    y_options = []
    # Verificand as possibilidades horizontais
    for y in range(len(matriz)):
        x_possibility = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for x in range(len(matriz)):
            if matriz[y][x] in x_possibility:
                x_possibility.remove(matriz[y][x])
        x_options.append(x_possibility)

    for y in range(len(matriz)):
        y_possibility = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for x in range(len(matriz)):
            if matriz[x][y] in y_possibility:
                y_possibility.remove(matriz[x][y])
        y_options.append(y_possibility)

    return show(x_options, y_options)


print(mostrar(board))
print('-' * 80)
validar(board)

