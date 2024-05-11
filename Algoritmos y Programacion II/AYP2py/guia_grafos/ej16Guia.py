# Implementar una función que reciba un grafo no dirigido y no pesado implementado con listas de adyacencia 
# (diccionario de diccionarios) y devuelva una matriz que sea equivalente a la representación de matriz de 
# adyacencia del mismo grafo. Indicar y justificar el orden del algoritmo implementado.

from grafo import Grafo

def matriz_de_adyacencia(grafo):
	vertices = grafo.obtener_vertices()
	n = len(grafo.obtener_vertices())
	matriz = []
	
	for _ in range(n):
		matriz.append([0]*n)

	for i in range(n):
		v = vertices[i]
		for j in range(n):
			if vertices[j] in grafo.adyacentes(v):
				matriz[i][j] = grafo.peso_arista(v, vertices[j])
	
	# for fila in matriz:
	# 	for c in fila:
	# 		print(c, end=" ")
	# 	print()
		
	return matriz


grafo1 = Grafo(False, ["A", "B", "C", "D", "E"])
grafo1.agregar_arista("A", "B")
grafo1.agregar_arista("A", "E")
grafo1.agregar_arista("B", "C")
grafo1.agregar_arista("B", "D")
grafo1.agregar_arista("B", "E")
grafo1.agregar_arista("C", "D")
matriz_de_adyacencia(grafo1)