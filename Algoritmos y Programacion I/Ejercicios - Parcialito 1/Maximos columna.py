def maximos_columnas(matriz):
	maximos = []
	for j in range(len(matriz[0])):
		columnas = []
		for i in range(len(matriz)):
			columnas.append(matriz[i][j])
		maximos.append(max(columnas))
	return maximos

