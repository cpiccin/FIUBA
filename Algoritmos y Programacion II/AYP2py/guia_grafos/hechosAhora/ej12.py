from grafo import Grafo


def puede_ser_no_dirigido(grafo):
	for v in grafo.obtener_vertices():
		for w in grafo.adyacentes(v):
			if v not in grafo.adyacentes(w):
				return False
	return True


grafo1 = Grafo(True, ["A", "B", "C", "D", "E"])
grafo1.agregar_arista("A", "C")
grafo1.agregar_arista("B", "A")
grafo1.agregar_arista("C", "D")
grafo1.agregar_arista("E", "C")
grafo1.agregar_arista("D", "E")
print(puede_ser_no_dirigido(grafo1))