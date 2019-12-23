matrix1 = [[1, -2], [-3, 4]]
matrix2 = [[2, -1], [0, -1]]

def add_old(matrixs1, matrixs2):
    rtn = []
    for lst1, lst2 in zip(matrixs1, matrixs2):
        rtn.append(list(map(lambda x, y: x + y, lst1, lst2)))

    return rtn

def add(*args):
    matrix_shapes = {
        tuple(len(r) for r in matrix)
        for matrix in args
    }
    if len(matrix_shapes) > 1:
        raise ValueError("Given matrices are not the same size.")
    rtn = []
    for rows in zip(*args):
        row = []
        for values in zip (*rows):
            row.append(sum(values))
        rtn.append(row)
    return rtn

if __name__ == "__main__":
    print(add(matrix1, matrix2))