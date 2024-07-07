from heap import MinHeap
from grafo import Grafo
import math


def caminos_minimos_dijkstra(grafo, origen):
	visitados = set()
	q = MinHeap()
	distancia = {}
	for v in grafo.obtener_vertices():
		distancia[v] = math.inf
	distancia[origen] = 0
	q.encolar(origen, 0)
	visitados.add(origen)
	while not q.esta_vacia():
		v = q.desencolar()
		for w in grafo.adyacentes(v):
			n = distancia[v] + grafo.peso_arista(v, w)
			if n < distancia[w]:
				distancia[w] = n 
				visitados.add(w)
				q.encolar(w, distancia[w])
	return distancia

# para poder aplicar dijkstra el grafo debe ser no dirigido y con pesos positivos
# si quedan vertices con distancia infinita significa que estan en otra componente conexa


grafo2 = Grafo(False, ["A", "B", "C", "D", "E", "F"])
grafo2.agregar_arista("A", "C", 5)
grafo2.agregar_arista("A", "B", 7)
grafo2.agregar_arista("A", "F", 8)
grafo2.agregar_arista("A", "E", 3)
grafo2.agregar_arista("B", "F", 3)
grafo2.agregar_arista("B", "E", 1)
grafo2.agregar_arista("C", "F", 2)
grafo2.agregar_arista("C", "E", 3)
grafo2.agregar_arista("C", "D", 5)
grafo2.agregar_arista("D", "E", 2)
print(caminos_minimos_dijkstra(grafo2, "A"))