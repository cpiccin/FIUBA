from grafo import Grafo
from collections import deque

def orden(grafo):
	orden = {}
	q = deque()
	res = []
	for v in grafo.obtener_vertices():
		orden[v] = 0
	for v in grafo.obtener_vertices():
		for w in grafo.adyacentes(v):
			orden[w] += 1
	for v in grafo.obtener_vertices():
		if orden[v] == 0:
			q.append(v)

	while q:
		v = q.popleft()
		res.append(v)
		for w in grafo.adyacentes(v):
			orden[w] -= 1
			if orden[w] == 0:
				q.append(w)

	if len(res) != len(grafo.obtener_vertices()):
		return None 

	return res