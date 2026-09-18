def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	rowam = len(a[0])
	colam = len(a)
	veclen = len(b)
	outvec = [0 for i in range(veclen)]
	if rowam != veclen:
		return -1
	else:
		for row in range(rowam):
			for el in range(colam):
				outvec[row] += a[row][el] * b[el]
	
	return outvec