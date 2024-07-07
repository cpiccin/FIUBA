# Implementar una función que reciba un grafo no dirigido y determine si el mismo no tiene ciclos de una cantidad impar
# de vértices. Indicar y justificar la complejidad de la función.

from grafo import Grafo


def tiene_ciclo(grafo):
	visitados = set()
	padre = {}
	ciclo = dfs_ciclo(grafo, grafo.vertice_aleatorio(), visitados, padre)
	return ciclo_es_impar(ciclo)


def dfs_ciclo(grafo, v, visitados, padre):
	visitados.add(v)
	for w in grafo.adyacentes(v):
		if w in visitados:
			if w != padre[v]:
				# esta en visitados y no es su padre
				return construye_ciclo(padre, w, v)
		else:
			padre[w] = v 
			ciclo = dfs_ciclo(grafo, w, visitados, padre)
			if ciclo != None:
				return ciclo

def construye_ciclo(padre, v, w):
	res = [v]
	while w != v:
		res.append(w)
		w = padre[w]
	return res


def ciclo_es_impar(ciclo):
	if len(ciclo) % 2 == 0:
		return True
	return False


grafo1 = Grafo(False, ["A", "B", "C", "D", "E", "F"])
grafo1.agregar_arista("A", "B")
grafo1.agregar_arista("B", "C")
grafo1.agregar_arista("C", "E")
grafo1.agregar_arista("D", "E")
grafo1.agregar_arista("F", "D")
grafo1.agregar_arista("C", "F")
print(tiene_ciclo(grafo1))