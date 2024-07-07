from grafo import Grafo
from collections import deque
import heapq, math


class MinHeap:
	def __init__(self):
		self.heap = []

	def encolar(self, item, prioridad):
		heapq.heappush(self.heap, (prioridad, item))

	def desencolar(self):
		if self.esta_vacia():
			raise IndexError("La cola esta vacia")
		return heapq.heappop(self.heap)[1]

	def esta_vacia(self):
		return len(self.heap) == 0



def caminos_minimos_dijkstra(grafo, origen, destino, peso):

	visitados = set()
	padre, distancia = {}, {}
	q = MinHeap()

	for v in grafo.obtener_vertices():
		distancia[v] = math.inf 

	visitados.add(origen)
	padre[origen], distancia[origen] = None, 0
	q.encolar(origen, distancia[origen])

	while not q.esta_vacia():
		v = q.desencolar()
		if not destino is None and v == destino:
			return padre, distancia
		for w in grafo.adyacentes(v):
			n = distancia[v] + grafo.peso_arista(v, w)[peso]
			if n < distancia[w]:
				distancia[w] = n 
				padre[w] = v
				q.encolar(w, distancia[w])

	if destino is None:
		return padre, distancia


def caminos_minimos_bfs(grafo, origen, destino, peso):

	visitados = set()
	padre, distancia = {}, {}
	q = deque()

	visitados.add(origen)
	padre[origen], distancia[origen] = None, 0
	q.append(origen)

	while q:
		v = q.popleft()
		if v == destino:
			return padre, distancia
		for w in grafo.adyacentes(v):
			if w not in visitados:
				visitados.add(w)
				padre[w] = v 
				distancia[w] = distancia[v] + 1
				q.append(w)


def orden_topologico_dfs(grafo):
	visitados = set()
	pila = deque()
	for v in grafo.obtener_vertices():
		if v not in visitados:
			orden_topologico_dfs_rec(grafo, v, pila, visitados)
	res = []
	while pila:
		res.append(pila.pop())
	return res 


def orden_topologico_dfs_rec(grafo, v, pila, visitados):
	visitados.add(v)
	for w in grafo.adyacentes(v):
		if w not in visitados:
			orden_topologico_dfs_rec(grafo, w, pila, visitados)
	pila.append(v)


def mst_prim(grafo, peso):
	origen = grafo.vertice_aleatorio()
	visitados = set()
	q = MinHeap()
	arbol = Grafo(False, grafo.obtener_vertices())
	visitados.add(origen)

	for w in grafo.adyacentes(origen):
		q.encolar((origen, w), grafo.peso_arista(origen, w)[peso])

	while not q.esta_vacia():
		v, w = q.desencolar()
		if w not in visitados:
			visitados.add(w)
			arbol.agregar_arista(v, w, grafo.peso_arista(v, w))
			for u in grafo.adyacentes(w):
				if u not in visitados:
					q.encolar((w, u), grafo.peso_arista(w, u)[peso])

	return arbol