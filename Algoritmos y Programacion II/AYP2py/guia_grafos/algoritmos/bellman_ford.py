from grafo import Grafo
import math

def caminos_minimos_bf(grafo, origen):
	dist = {}
	padre = {}
	for v in grafo.obtener_vertices():
		dist[v] = math.inf 

	dist[origen] = 0
	padre[origen] = None
	aristas = grafo.obtener_aristas()

	for i in range(len(grafo.obtener_vertices())):

		for v,w,p in aristas:
			if dist[v] + p < dist[w]:
				dist[w] = dist[v] + p
				padre[w] = v 

	for v,w,p in aristas:
		# para reconocer un ciclo
		if dist[v] + p < dist[w]:
			return None

	return padre, dist


grafo2 = Grafo(True, ["A", "B", "C", "D", "E", "F", "G", "H"])
grafo2.agregar_arista("B", "A", 7)
grafo2.agregar_arista("F", "B", 1)
grafo2.agregar_arista("A", "F", 3)
grafo2.agregar_arista("A", "D", -4)
grafo2.agregar_arista("A", "C", -1)
grafo2.agregar_arista("A", "G", -5)
grafo2.agregar_arista("D", "F", 1)
grafo2.agregar_arista("C", "H", 5)
grafo2.agregar_arista("D", "H", 8)
grafo2.agregar_arista("G", "C", 2)
grafo2.agregar_arista("C", "G", -1)
grafo2.agregar_arista("G", "E", 3)

punto_inicial = "A"

padres, distancias = caminos_minimos_bf(grafo2, punto_inicial)

print("PADRES: ", padres)
print("DISTANCIAS: ", distancias)