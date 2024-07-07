from grafo import Grafo
from collections import deque

def es_arbol(grafo):
	aristas, vertices = 0, 0
	for a in grafo.obtener_aristas():
		aristas += 1
	for v in grafo.obtener_vertices():
		vertices += 1
	if aristas != vertices-1:
		return False
	visitados = set()
	q = deque()
	origen = grafo.vertice_aleatorio()
	q.append(origen)
	visitados.add(origen)
	while q:
		v = q.popleft()
		for w in grafo.adyacentes(v):
			if w not in visitados:
				visitados.add(w)
				q.append(w)
	for v in grafo.obtener_vertices():
		if v not in visitados:
			return False # es conexo
	return True


grafo1 = Grafo(False, [1,2,3,4,5,6])
grafo1.agregar_arista(1, 3)
grafo1.agregar_arista(2, 1)
grafo1.agregar_arista(2, 6)
grafo1.agregar_arista(5, 2)
grafo1.agregar_arista(4, 2)
print(es_arbol(grafo1))
