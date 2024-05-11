from grafo import Grafo
from heap import MinHeap

# Algoritmo de Prim para obtener el arbol de tendido minimo (MST).
# Implementado con un heap de minimos

def mst_prim(grafo):

	origen = grafo.vertice_aleatorio()
	visitados = set()
	q = MinHeap()
	arbol = Grafo(False, grafo.obtener_vertices())
	
	visitados.add(origen)
	for w in grafo.adyacentes(origen):
		q.encolar((origen, w), grafo.peso_arista(origen, w))

	while not q.esta_vacia():
		v, w = q.desencolar()
		if w not in visitados:
			visitados.add(w)
			arbol.agregar_arista(v, w, grafo.peso_arista(v, w))
			for u in grafo.adyacentes(w):
				if u not in visitados:
					q.encolar((w, u), grafo.peso_arista(w, u))

	return arbol


grafo1 = Grafo(False, ["A", "B", "C"])
grafo1.agregar_arista("A", "B", 2)
grafo1.agregar_arista("A", "C", 3)
grafo1.agregar_arista("B", "C", 2)
print(mst_prim(grafo1))