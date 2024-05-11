from grafo import Grafo
from UnionFind import UnionFind

# Algoritmo de Kruskal para obtener el arbol de tendido minimo de un grafo
# Utiliza el TDA UnionFind para verificar de forma eficiente si dos vertices
# estan en la misma componente conexa

def mst_kruskal(grafo):

	conjuntos = UnionFind(grafo.obtener_vertices())
	aristas = grafo.obtener_aristas()
	arbol = Grafo(False, grafo.obtener_vertices())
	aristas.sort(key=lambda x: x[2])
	for arista in aristas:
		v, w, p = arista
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
