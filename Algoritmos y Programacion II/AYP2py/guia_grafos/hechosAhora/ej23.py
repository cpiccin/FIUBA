def diametro_red(grafo):
	visitados = set()
	distancia = {}
	origen = grafo.vertice_aleatorio()
	q = deque()
	distancia[origen] = 0
	visitados.add(origen)
	q.append(origen)
	while q:
		v = q.popleft()
		for w in grafo.adyacentes(v):
			if w not in visitados:
				q.append(w)
				distancia[w] = distancia[v]+1
				visitados.add(w)
	diametro = 0
	for v in distancia:
		if distancia[v] > diametro:
			diametro = distancia[v]
	return diametro