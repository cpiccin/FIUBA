# Implementar una función que permita determinar si un grafo puede ser no dirigido. 
# Determinar el orden del algoritmo implementado.

from grafo import Grafo

def puede_ser_no_dirigido(grafo):
	for v in grafo.obtener_vertices():
		for w in grafo.adyacentes(v):
			if v not in grafo.adyacentes(w):
				return False
	return True


grafo1 = Grafo(True, ["A", "C", "B"])
grafo1.agregar_arista("A", "B")
grafo1.agregar_arista("B", "A")
grafo1.agregar_arista("C", "A")
# grafo1.agregar_arista("A", "C")
print(puede_ser_no_dirigido(grafo1))