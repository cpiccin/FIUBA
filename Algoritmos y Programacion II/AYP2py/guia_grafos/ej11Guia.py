# Implementar un algoritmo que reciba un grafo dirigido, un vértice V y un número N, y devuelva una lista 
# con todos los vértices que se encuentren a exactamente N aristas de distancia del vértice V. 
# Indicar el tipo de recorrido utilizado y el orden del algoritmo. Justificar.

from grafo import Grafo
from collections import deque

# recibe grafo dirigido, un vertice V y un numero N

def distancia(grafo, v, n):
	distancia = {}
	visitados = set()
	q = deque()
	q.append(v)
	distancia[v] = 0 
	visitados.add(v)

	# BFS
	while q:
		vertice = q.popleft()
		for w in grafo.adyacentes(vertice):
			if w not in visitados:
				visitados.add(w)
				distancia[w] = distancia[vertice] + 1
				q.append(w)
	res = []
	for vertice in distancia:
		if distancia[vertice] == n:
			res.append(vertice)
	return res


grafo1 = Grafo(False, ["A", "B", "C", "D", "E", "F", "G"])
grafo1.agregar_arista("B", "A")
grafo1.agregar_arista("B", "C")
grafo1.agregar_arista("B", "D")
grafo1.agregar_arista("C", "D")
grafo1.agregar_arista("D", "F")
grafo1.agregar_arista("D", "E")
grafo1.agregar_arista("E", "F")
grafo1.agregar_arista("F", "G")
print(distancia(grafo1, "A", 4))