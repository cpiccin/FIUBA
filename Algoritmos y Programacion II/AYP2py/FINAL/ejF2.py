# Escribir el Algoritmo de Kruskal para obtener el árbol de tendido mínimo de un grafo no dirigido y pesado. Si al escribir
# el algoritmo, sabemos que en el/los grafos que se va a aplicar los pesos fueran menores a 100, ¿cuál sería la complejidad
# de dicho algoritmo?


from UnionFind import union,find
from heap import MinHeap
from grafo import Grafo


def mst_kruskal(grafo):
	aristas = grafo.obtener_aristas()
	conjuntos = UnionFind(grafo.obtener_vertices())
	q = MinHeap()
	res = Grafo(False, grafo.obtener_vertices())
	for v,w,p in aristas: 
		q.encolar((v, w), p)
	for i in range(len(grafo.obtener_vertices())):
		v, w = q.desencolar()
		if conjuntos.find(v) == conjuntos.find(w):
			# estan en el mismo grupo
			continue
		res.agregar_arista(v, w, grafo.peso_arista(v, w))
		conjuntos.union(v, w)