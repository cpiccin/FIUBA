from grafo import Grafo


def museo(grafo):
	res = []
	visitados = set()
	origen = grafo.vertice_aleatorio()
	res.append(origen)
	res = DFS(grafo, visitados, origen, res)
	return res

def DFS(grafo, visitados, v, res):
	visitados.add(v)
	for w in grafo.adyacentes(v):
		if w not in visitados:
			res.append(w)
			res = DFS(grafo, visitados, w, res)
	return res 

grafo1 = Grafo(False, [1,2,3,4,5,6,7])
grafo1.agregar_arista(1, 2)
grafo1.agregar_arista(2, 3)
grafo1.agregar_arista(3, 7)
grafo1.agregar_arista(2, 4)
grafo1.agregar_arista(2, 7)
grafo1.agregar_arista(7, 4)
grafo1.agregar_arista(5, 3)
grafo1.agregar_arista(5, 6)
grafo1.agregar_arista(4, 6)
print(museo(grafo1))