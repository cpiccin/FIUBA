from grafo import Grafo
from heap import MinHeap
import math


def caminos_minimos_dijkstra(grafo, origen):
	distancia = {}
	padre = {}

	for v in grafo.obtener_vertices():
		distancia[v] = math.inf

	distancia[origen] = 0
	padre[origen] = None
	q = MinHeap()
	q.encolar(origen, 0)

	while not q.esta_vacia():
		v = q.desencolar()

		for w in grafo.adyacentes(v):
			n = distancia[v] + grafo.peso_arista(v, w)
			if n < distancia[w]:
				distancia[w] = n
				padre[w] = v
				q.encolar(w, distancia[w])
				
	return padre, distancia

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


punto_inicial = "A"
padres, distancias = caminos_minimos_dijkstra(grafo2, punto_inicial)
print("PADRES: ", padres)
print("DISTANCIAS: ", distancias)