# devuelve un ciclo

from grafo import Grafo

# con DFS
def obtener_ciclo_dfs(grafo):
	visitados = set()
	padre = {}
	for v in grafo.obtener_vertices():
		if v not in visitados:
			ciclo = obtiene_ciclo_dfs(grafo, v, visitados, padre)
			if ciclo is not None:
				return ciclo
	return None 

def obtiene_ciclo_dfs(grafo, v, visitados, padre):
	visitados.add(v)
	for w in grafo.adyacentes(v):
		if w in visitados:
			if w != padre[v]:
				return reconstruye_ciclo(padre, w, v)
		else: # no esta en visitados
			padre[w] = v 
			ciclo = obtiene_ciclo_dfs(grafo, w, visitados, padre)
			if ciclo is not None:
				return ciclo  

	return None

def reconstruye_ciclo(padre, ini, fin):
	v = fin
	ciclo = []
	while v != ini:
		ciclo.append(v)
		v = padre[v]
	ciclo.append(ini)
	return ciclo[::-1]

g = Grafo(True, ["A", "B", "C", "D", "E"])
g.agregar_arista("A", "B")
g.agregar_arista("A", "C")
g.agregar_arista("C", "B")
g.agregar_arista("C", "E")
g.agregar_arista("E", "D")
g.agregar_arista("D", "C")

print(obtener_ciclo_dfs(g))