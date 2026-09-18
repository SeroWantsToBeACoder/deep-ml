def vector_sum(a: list[int|float], b: list[int|float]) -> list[int|float]:
	len_a = len(a)
	len_b = len(b)
	if len_a == len_b:
		out = []
		for i in range(0, len_a):
			out.append(a[i] + b[i])
		return out
	else:
		return -1
