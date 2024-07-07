from grafo import Grafo
from heap import MinHeap
from UnionFind import UnionFind

# Algoritmo de Kruskal para obtener el arbol de tendido minimo de un grafo
# Utiliza el TDA UnionFind para verificar de forma eficiente si dos vertices
# estan en la misma componente conexa

def mst_kruskal(grafo):

	conjuntos = UnionFind(grafo.obtener_vertices())
	aristas = grafo.obtener_aristas()
	arbol = Grafo(False, grafo.obtener_vertices())
	q = MinHeap()
	for a in aristas:
		q.encolar(a[:2], a[2])
	for i in range(len(aristas)):
		v, w = q.desencolar()
		if conjuntos.find(v) == conjuntos.find(w): # si son iguales pertenecen al mismo conjunto
			continue # estan en la misma componente conexa
		arbol.agregar_arista(v, w, p)
		conjuntos.union(v, w)
	
	return arbol 


grafo1 = Grafo(False, ["A", "B", "C"])
grafo1.agregar_arista("A", "B", 2)
grafo1.agregar_arista("A", "C", 3)
grafo1.agregar_arista("B", "C", 2)
print(mst_kruskal(grafo1))
