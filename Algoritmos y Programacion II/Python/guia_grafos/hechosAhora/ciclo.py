from grafo import Grafo

g = Grafo(True, ["A", "B", "C", "D", "E"])
g.agregar_arista("A", "B")
g.agregar_arista("A", "C")
g.agregar_arista("C", "B")
g.agregar_arista("C", "E")
g.agregar_arista("E", "D")
g.agregar_arista("D", "C")

def ciclo(grafo):
	visitados, padre = set(), {}
	for v in grafo.obtener_vertices():
		padre[v] = None 
	for v in grafo.obtener_vertices():
		if v not in visitados:
			ciclo = dfs_ciclo(grafo, v, visitados, padre)
			if ciclo != None:
				return ciclo
	return None

def dfs_ciclo(grafo, v, visitados, padre):
	visitados.add(v)
	for w in grafo.adyacentes(v):
		if w in visitados:
			if w != padre[v] and len(grafo.adyacentes(w)) != 0:
				return reconstruye_ciclo(padre, w, v)
		else:
			padre[w] = v 
			ciclo = dfs_ciclo(grafo, w, visitados, padre)
			if ciclo != None:
				return ciclo
	return None 

def reconstruye_ciclo(padre, ini, fin):
	v = fin 
	res = []
	print(padre)
	while v != ini:
		res.append(v)
		v = padre[v]
	res.append(ini)
	return res[::-1]

print(ciclo(g))