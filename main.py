from functools import reduce
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


# TODO Refatorar para poder apresentar de maneira melhor
def show(*args):
    linha = 1
    for elements in range(len(args)):
        print('-'*80)
        for sub_elements in range(len(args[elements])):
            print(f'{args[elements][sub_elements]}')
        linha += 1


# TODO Refatorar o código para evitar repetição de estruturas e laços desnecessários.
def validar(matriz):
    x_options = []
    y_options = []
    # Verificando as possibilidades horizontais
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

    show(board, x_options, y_options)
    return solve(board, x_options, y_options)


def solve(matriz, horizontal_list, vertical_list):
    print('=' * 30)
    for x in range(len(matriz)):
        for y in range(len(matriz[x])):
            if matriz[y][x] == 0:
                duplicate_numbers = [*horizontal_list[x], *vertical_list[y]]
                print(duplicate_numbers)
            else:
                continue

print('-' * 80)
validar(board)
