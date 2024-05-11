# a) grado de todos los vertices de un no dirigido

from grafo import Grafo

def grados_no_dirigido(grafo):
	grados = {}
	for v in grafo.obtener_vertices():
		for w in grafo.adyacentes(v):
			if v not in grados:
				grados[v] = 0
			grados[v] += 1
	return grados


def grados_salida_dirigido(grafo):
	return grados_no_dirigido(grafo)

def grados_entrada_dirigido(grafo):
	grados = {}
	for v in grafo.obtener_vertices():
		for w in grafo.adyacentes(v):
			if w not in grados:
				grados[w] = 0
			grados[w] += 1
	return grados



grafo1 = Grafo(True, ["A", "B", "C", "D", "E"])
grafo1.agregar_arista("A", "C")
grafo1.agregar_arista("B", "A")
grafo1.agregar_arista("C", "D")
grafo1.agregar_arista("E", "C")
grafo1.agregar_arista("C", "E")
grafo1.agregar_arista("D", "E")
print(grados_entrada_dirigido(grafo1))