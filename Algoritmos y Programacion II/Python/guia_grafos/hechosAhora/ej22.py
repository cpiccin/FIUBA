from grafo import Grafo


def ciclo_impar(grafo):
	visitados = set()
	padre = {}
	ciclo = obtener_ciclo(grafo, visitados, padre)
	if len(ciclo) % 2 == 0:
		return True 
	return False


def obtener_ciclo(grafo, visitados, padre):
	for v in grafo.obtener_vertices():
		if v not in visitados:
			ciclo = dfs_ciclo(grafo, visitados, padre, v)
			if ciclo != None:
				return ciclo 
	return None

def dfs_ciclo(grafo, visitados, padre, v):
	visitados.add(v)
	for w in grafo.adyacentes(v):
		if w in visitados:
			if w != padre[v]:
				return construye_ciclo(padre, w, v)
		else:
			padre[w] = v
			ciclo = dfs_ciclo(grafo, visitados, padre, w)
			if ciclo != None:
				return ciclo
	return None


def construye_ciclo(padre, ini, fin):
	v = fin 
	res = []
	while v != ini:
		res.append(v)
		v = padre[v] # va de hijo a padre
 	res.append(v)
 	return res[::-1]

