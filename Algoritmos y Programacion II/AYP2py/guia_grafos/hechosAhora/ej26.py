from grafo import Grafo
from heap import MinHeap
from UnionFind import UnionFind

# obtener mst del grafo

# a) con Prim

def mst_prim(grafo):
	origen = grafo.vertice_aleatorio()
	q = MinHeap()
	visitados = set()
	res = Grafo(False, grafo.obtener_vertices())
	for w in grafo.adyacentes(origen):
		q.encolar((origen, w), grafo.peso_arista(origen, w))
	while not q.esta_vacia():
		v, w = q.desencolar()
		if w in visitados:
			continue
		res.agregar_arista(v, w, grafo.peso_arista(v, w))
		visitados.add(w)
		for ady in grafo.adyacentes(w):
			if ady not in visitados:
				q.encolar((w, ady), grafo.peso_arista(w, ady))
	return res

# b) con Kruskal

def mst_kruskal(grafo):
	conjuntos = UnionFind(grafo.obtener_vertices())
	aristas = grafo.obtener_aristas()
	res = Grafo(False, grafo.obtener_vertices())
	q = MinHeap()
	for a in aristas:
		q.encolar(a, a[2])
	for i in range(len(aristas)):
		v, w, peso = q.desencolar()
		if conjuntos.find(v) == conjuntos.find(w): # estan en la misma comp conexa
			continue
		res.agregar_arista(v, w, peso)
		conjuntos.union(v, w)
	return res


grafo1 = Grafo(False, ["A", "B", "C", "D", "E", "F", "G", "H", "I"])
grafo1.agregar_arista("B", "A", 5)
grafo1.agregar_arista("B", "F", 1)
grafo1.agregar_arista("F", "A", 8)
grafo1.agregar_arista("F", "D", 6)
grafo1.agregar_arista("D", "C", 8)
grafo1.agregar_arista("D", "H", 6)
grafo1.agregar_arista("C", "A", 7)
grafo1.agregar_arista("C", "H", 3)
grafo1.agregar_arista("C", "E", 3)
grafo1.agregar_arista("H", "I", 2)
grafo1.agregar_arista("I", "E", 3)
grafo1.agregar_arista("E", "A", 2)
grafo1.agregar_arista("E", "G", 3)
grafo1.agregar_arista("G", "A", 4)

print("PRIM: \n", mst_prim(grafo1))
print("KRUSKAL:\n", mst_kruskal(grafo1))
