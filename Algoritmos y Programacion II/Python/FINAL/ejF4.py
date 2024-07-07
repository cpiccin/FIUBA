def ptos_art(grafo):
	origen = grafo.vertice_aleatorio()
	visitados, padre, orden, mas_bajo, res, es_raiz = set(), {origen:None}, {origen:0}, {}, set(), True
	visitados.add(origen)
	ptos_art_dfs(grafo, origen, visitados, padre, orden, mas_bajo, res, es_raiz)
	return res 

def ptos_art_dfs(grafo, v, visitados, padre, orden, mas_bajo, res, es_raiz):
	hijos = 0
	mas_bajo[v] = orden[v]
	for w in grafo.adyacentes(v):
		if w not in visitados:
			visitados.add(w)
			hijos += 1
			orden[w] = orden[v] + 1
			padre[w] = v
			ptos_art_dfs(grafo, w, visitados, padre, orden, mas_bajo, res, False)
			if mas_bajo[w] >= orden[v] and not es_raiz:
				res.add(v)
			mas_bajo[v] = min(mas_bajo[v], mas_bajo[w])
		elif padre[v] != w:
			mas_bajo[v] = min(mas_bajo[v], orden[w])
	if es_raiz and hijos > 1:
		res.add(v)