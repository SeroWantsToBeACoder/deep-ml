import numpy as np

def cosine_similarity(v1, v2):
	v1v2 = 0
	dim = len(v1)
	for a in range(dim):
		v1v2 += v1[a]*v2[a]
	
	bv1 = 0
	for el in v1:
		bv1 += pow(el, 2)
	bv1 = np.sqrt(bv1)

	bv2 = 0
	for el in v2:
		bv2 += pow(el, 2)
	bv2 = np.sqrt(bv2)

	cs = v1v2/(bv1*bv2)

	return round(cs, 3)
