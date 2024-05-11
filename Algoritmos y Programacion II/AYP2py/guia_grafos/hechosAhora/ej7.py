from grafo import Grafo

def grafo_transpuesto(grafo):
	res = Grafo(True, grafo.obtener_vertices())
	for v in grafo.obtener_vertices():
		for w in grafo.adyacentes(v):
			res.agregar_arista(w, v)
	return res 


grafo1 = Grafo(True, ["A", "B", "C", "D", "E"])
grafo1.agregar_arista("A", "C")
grafo1.agregar_arista("B", "A")
grafo1.agregar_arista("C", "D")
grafo1.agregar_arista("E", "C")

grafo1.agregar_arista("D", "E")
print(grafo_transpuesto(grafo1))