# El diámetro de una red es el máximo de las distancias mínimas entre todos los vértices de la misma. 
# Implementar un algoritmo que permita obtener el diámetro de una red, para el caso de un grafo no dirigido y no pesado. 
# Indicar el orden del algoritmo propuesto.

# Maximo de las distancias minimas en un grafo no dirigido y no pesado es la distancia maxima de un dicc de orden de un BFS

from grafo import Grafo
from collections import deque

def diametro_red(grafo):
	visitados = set()
	distancias = {}
	origen = grafo.vertice_aleatorio()
	
	q = deque()
	visitados.add(origen)
	q.append(origen)
	distancias[origen] = 0

	while q:
		v = q.popleft()
		for w in grafo.adyacentes(v):
			if w not in visitados:
				q.append(w)
				visitados.add(w)
				distancias[w] = distancias[v] + 1

	return max(distancias)

def max(distancias):
	res = 0
	for v in distancias:
		if distancias[v] > res:
			res = distancias[v]
	return res

grafo1 = Grafo(False, ["A", "B", "C", "D", "E", "F", "G"])
grafo1.agregar_arista("A", "B")
grafo1.agregar_arista("D", "F")
grafo1.agregar_arista("B", "C")
grafo1.agregar_arista("C", "F")
grafo1.agregar_arista("B", "E")
grafo1.agregar_arista("E", "D")
grafo1.agregar_arista("D", "B")
# grafo1.agregar_arista("F", "G")
print(diametro_red(grafo1))