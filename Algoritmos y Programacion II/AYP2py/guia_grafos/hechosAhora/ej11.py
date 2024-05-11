from grafo import Grafo
from collections import deque

def a_n_aristas(grafo, origen, n):
	res = []
	visitados = set()
	distancia = {}
	q = deque()
	q.append(origen)
	visitados.add(origen)
	distancia[origen] = 0

	while q:
		v = q.popleft()
		for w in grafo.adyacentes(v):
			if w not in visitados:
				visitados.add(w)
				distancia[w] = distancia[v]+1
				q.append(w)

	for v in distancia:
		if distancia[v] == n:
			res.append(v)

	return res


grafo1 = Grafo(False, ["A" , "B", "C", "D", "E", "F"])
grafo1.agregar_arista("A", "B")
grafo1.agregar_arista("C", "A")
grafo1.agregar_arista("C", "D")
grafo1.agregar_arista("E", "C")
grafo1.agregar_arista("D", "E")
grafo1.agregar_arista("F", "D")
print(a_n_aristas(grafo1, "A", 3))
