def pos_i(A, B):
	lista_tuplas = []
	for i in range(len(A)):
		lista_tuplas.append((A[i], B[i]))
	return lista_tuplas


print(pos_i([1, 2, 3], [4, 5, 6]))