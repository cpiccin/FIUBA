from grafo import Grafo
import math

def caminos_minimos_bf(grafo, origen):
	distancia = {}
	
	for v in grafo.obtener_vertices():
		distancia[v] = math.inf
	distancia[origen] = 0
	
	aristas = grafo.obtener_aristas()
	for _ in range(len(grafo.obtener_vertices())):
		for v, w, peso in aristas: 
			n = distancia[v] + peso
			if n < distancia[w]:
				distancia[w] = n 
	# para reconocer un ciclo negativo
	for v, w, peso in aristas:
		if distancia[v] + peso < distancia[w]:
			return None 

	return distancia


grafo1 = Grafo(True, ["A", "B", "C", "D", "E", "F", "G", "H"])
#grafo1.agregar_arista("B", "A", 7)
grafo1.agregar_arista("B", "A", 1)
grafo1.agregar_arista("A", "G", -5)
grafo1.agregar_arista("A", "C", -1)
grafo1.agregar_arista("A", "D", -4)
grafo1.agregar_arista("A", "F", 3)
grafo1.agregar_arista("F", "B", 1)
grafo1.agregar_arista("D", "F", 1)
grafo1.agregar_arista("D", "H", 8)
grafo1.agregar_arista("C", "H", 5)
grafo1.agregar_arista("C", "G", -1)
grafo1.agregar_arista("G", "C", 2)
grafo1.agregar_arista("G", "E", 3)
print(caminos_minimos_bf(grafo1, "A"))