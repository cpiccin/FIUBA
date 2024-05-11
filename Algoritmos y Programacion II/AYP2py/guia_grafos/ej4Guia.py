# Implementar un algoritmo que determine si un grafo no dirigido es conexo o no. 
# Indicar la complejidad del algoritmo si el grafo está implementado con una matriz de adyacencia.


from grafo import Grafo
from collections import deque

def es_conexo(grafo):
	visitados = set()
	padre = {}
	q = []
	origen = grafo.vertice_aleatorio()
	padre[origen] = None
	q.append(origen)
	while len(q) > 0:
		v = q[0]
		q = q[1:]
		for w in grafo.adyacentes(v):
			if w not in visitados:
				visitados.add(w)
				padre[w] = v
				q.append(w)
	for v in grafo.obtener_vertices():
		if v not in visitados:
			# hay una componente que no visito el BFS
			return False
	return True

grafo_no_dirigido = Grafo(False, ["A", "B", "C", "D", "E"])
grafo_no_dirigido.agregar_arista("A", "B")
grafo_no_dirigido.agregar_arista("B", "E")
# grafo_no_dirigido.agregar_arista("B", "C")
grafo_no_dirigido.agregar_arista("D", "B")
grafo_no_dirigido.agregar_arista("E", "D")
print(grafo_no_dirigido)

print(es_conexo(grafo_no_dirigido))