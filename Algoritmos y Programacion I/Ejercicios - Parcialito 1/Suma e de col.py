def suma_columnas(matriz):
	lista_sumas = []
	suma = 0
	for j in range(len(matriz[0])):
		for i in range(len(matriz)):
			suma += matriz[i][j]
		lista_sumas.append(suma)
		suma = 0
	return lista_sumas


print(suma_columnas([
    [1, 2, 3, 0],
    [4, 5, 6, 10],
    [7, 8, 9, -3]
]))
