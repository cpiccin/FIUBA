# Implementar una función que determine el:

# a. El grado de todos los vértices de un grafo no dirigido.

# b. El grado de salida de todos los vértices de un grafo dirigido.

# c. El grado de entrada de todos los vértices de un grafo dirigido.

from grafo import Grafo

def grados_no_dirigido(grafo):
	grados = {}
	for v in grafo.obtener_vertices():
		grados[v] = 0 
		for w in grafo.adyacentes(v):
			grados[v] += 1
	return grados


# grafo_no_dirigido = Grafo(False, ["A", "B", "C", "D", "E"])
# grafo_no_dirigido.agregar_arista("A", "B")
# grafo_no_dirigido.agregar_arista("B", "E")
# grafo_no_dirigido.agregar_arista("B", "C")
# grafo_no_dirigido.agregar_arista("D", "B")
# grafo_no_dirigido.agregar_arista("E", "D")

# print(grafo_no_dirigido)
# print(grados_no_dirigido(grafo_no_dirigido))

def g_salida_dirigido(grafo):
	grados = {}
	for v in grafo.obtener_vertices():
		grados[v] = 0
		for w in grafo.adyacentes(v):
			grados[v] += 1
	return grados


# grafo_dirigido = Grafo(True, ["A", "B", "C", "D", "E"])
# grafo_dirigido.agregar_arista("A", "B")
# grafo_dirigido.agregar_arista("B", "E")
# grafo_dirigido.agregar_arista("B", "C")
# grafo_dirigido.agregar_arista("D", "B")
# grafo_dirigido.agregar_arista("E", "D")
# print(grafo_dirigido)
# print(g_salida_dirigido(grafo_dirigido))


def g_entrada_dirigido(grafo):
	grados = {}
	for v in grafo.obtener_vertices():
		for w in grafo.adyacentes(v):
			if w not in grados:
				grados[w] = 0
			grados[w] += 1
		if v not in grados:
			grados[v] = 0
	return grados

# grafo_dirigido = Grafo(True, ["A", "B", "C", "D", "E"])
# grafo_dirigido.agregar_arista("A", "B")
# grafo_dirigido.agregar_arista("B", "E")
# grafo_dirigido.agregar_arista("B", "C")
# grafo_dirigido.agregar_arista("D", "B")
# grafo_dirigido.agregar_arista("E", "D")
# print(grafo_dirigido)
# print(g_entrada_dirigido(grafo_dirigido))