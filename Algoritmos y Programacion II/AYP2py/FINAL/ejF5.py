from grafo import Grafo
from collections import deque
import math

def bfs_modificado(grafo, origen):
	distancia = {}
	for v in grafo.obtener_vertices():
		distancia[v] = math.inf 
	distancia[origen] = 0
	q = deque()
	q.append(origen)
	while q:
		v = q.popleft()
		for w in grafo.adyacentes(v):
			n = distancia[v] + grafo.peso_arista(v, w)
			if n < distancia[w]:
				distancia[w] = n 
				q.append(w)
	return distancia

grafo1 = Grafo(False, ["A", "B", "C", "D", "E", "F"])
grafo1.agregar_arista("A", "F", 1)
grafo1.agregar_arista("F", "C", 1)
grafo1.agregar_arista("C", "E", 1)
grafo1.agregar_arista("C", "D", 1)
grafo1.agregar_arista("D", "E", 2)
grafo1.agregar_arista("C", "B", 2)
grafo1.agregar_arista("D", "B", 2)
grafo1.agregar_arista("A", "B", 2)

print(bfs_modificado(grafo1, "A"))