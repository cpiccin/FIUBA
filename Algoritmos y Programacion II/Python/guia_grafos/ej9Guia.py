from grafo import Grafo


def recorrido_salas(grafo):
	visitados = set()
	padre = {}
	origen = grafo.vertice_aleatorio()
	padre[origen] = None
	res = []
	return dfs_recorrido(grafo, origen, visitados, padre, res) 

def dfs_recorrido(g, v, visitados, padre, res):
	visitados.add(v)
	for w in g.adyacentes(v):
		if w not in res:
			res.append(w)
		if w not in visitados:
			padre[w] = v
			dfs_recorrido(g, w, visitados, padre, res)
	return res


grafo1 = Grafo(False, ["E", "B", "A", "G", "D", "F", "C", "H"])
grafo1.agregar_arista("E", "B")
grafo1.agregar_arista("E", "G")
grafo1.agregar_arista("A", "G")
grafo1.agregar_arista("A", "B")
grafo1.agregar_arista("D", "A")
grafo1.agregar_arista("D", "F")
grafo1.agregar_arista("F", "C")
grafo1.agregar_arista("C", "H")
print(recorrido_salas(grafo1))