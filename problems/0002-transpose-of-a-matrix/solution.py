def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    rowam = len(a)
    colam = len(a[0])
    out_mat = [[0 for x in range(rowam)] for x in range(colam)]

    for row in range(rowam):
        for col in range(colam):
            out_mat[col][row] = a[row][col]
    
    return out_mat