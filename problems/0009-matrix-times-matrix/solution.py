def matrixmul(a:list[list[int|float]], b:list[list[int|float]])-> list[list[int|float]]:
    mat_a_row = len(a)
    mat_a_col = len(a[0])
    mat_b_row = len(b)
    mat_b_col = len(b[0])
    outmat = [[0 for i in range(mat_b_col)] for i in range(mat_a_row)]

    if mat_a_col != mat_b_row:
        return -1
    else:
        for row in range(mat_a_row):
            for col in range(mat_b_col):
                for el in range(mat_a_col):
                    outmat[row][col] += a[row][el] * b[el][col]

    return outmat
    