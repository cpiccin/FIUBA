from grafo import Grafo
from collections import deque

def es_conexo(grafo):
	visitados = set()
	origen = grafo.vertice_aleatorio()
	q = []
	q.append(origen)
	visitados.add(origen)
	while q:
		v = q[0]
		q = q[1:]
		for w in grafo.adyacentes(v):
			if w not in visitados:
				visitados.add(w)
				q.append(w)
	for v in grafo.obtener_vertices():
		if v not in visitados:
			return False
	return True

grafo1 = Grafo(False, ["A" , "B", "C", "D", "E"])
grafo1.agregar_arista("A", "B")
grafo1.agregar_arista("C", "A")
grafo1.agregar_arista("C", "D")
grafo1.agregar_arista("E", "C")
grafo1.agregar_arista("D", "E")
print(es_conexo(grafo1))