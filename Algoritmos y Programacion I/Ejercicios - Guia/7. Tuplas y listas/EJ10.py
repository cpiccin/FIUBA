# a) Escribir una función que reciba dos matrices y devuelva la suma. Las matrices están representadas como listas de listas.
MATRIZ1 = [[1,0],[3,4]]
MATRIZ2 = [[1,1],[1,1]]

def suma_matrices(m1, m2):
	matriz = []
	for i in range(len(m1[0])):
		fila_i = []
		for j in range(len(m1[0])):
			fila_i.append(m1[i][j]+m2[i][j])
		matriz.append(fila_i)
	return matriz

# b) Escribir una función que reciba dos matrices y devuelva el producto. Las matrices están representadas como listas de listas.

def multiplica_matrices(m1, m2):
