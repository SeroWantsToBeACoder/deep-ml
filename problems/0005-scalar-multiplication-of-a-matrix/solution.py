def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
	rowam = len(matrix)
	colam = len(matrix[0])
	outmat = matrix

	for row in range(rowam):
		for el in range(colam):
			outmat[row][el] = outmat[row][el] * scalar

	return outmat