# Un autor decidió escribir un libro con varias tramas que se puede leer de forma no lineal. 
# Es decir, por ejemplo, después del capítulo 1 puede leer el 2 o el 73; pero la historia no 
# tiene sentido si se abordan estos últimos antes que el 1.

# Siendo un aficionado de la computación, el autor ahora necesita un orden para publicar su obra, 
# y decidió modelar este problema como un grafo dirigido, en dónde los capítulos son los vértices 
# y sus dependencias las aristas. Así existen, por ejemplo, las aristas (v1, v2) y (v1, v73).

# Escribir un algoritmo que devuelva un orden en el que se puede leer la historia sin obviar ningún capítulo. 
# Indicar la complejidad del algoritmo.


from grafo import Grafo
from collections import deque

def orden_libros(grafo):
	grados = {}
	res = []
	
	for v in grafo.obtener_vertices():
		grados[v] = 0 
	
	for v in grafo.obtener_vertices():
		for w in grafo.adyacentes(v):
			grados[w] += 1
	
	q = deque()
	for v in grafo.obtener_vertices():
		if grados[v] == 0:
			q.append(v)

	while q:
		v = q.popleft()
		res.append(v)
		for w in grafo.adyacentes(v):
			grados[w] -= 1
			if grados[w] == 0:
				q.append(w)

	if len(res) == len(grafo.obtener_vertices()):
		return res
	return None


grafo1 = Grafo(True, ["v1", "v2", "v3", "v73", "v7"])
grafo1.agregar_arista("v1", "v2")
grafo1.agregar_arista("v1", "v73")
grafo1.agregar_arista("v2", "v3")
grafo1.agregar_arista("v7", "v73")
print(orden_libros(grafo1))