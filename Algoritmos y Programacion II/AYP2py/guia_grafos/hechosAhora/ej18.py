

def minima_cantidad(grafo, x, y):
	visitados = set()
	distancia = {}
	q = deque()
	visitados.add(x)
	distancia[x] = 0
	q.append(x)

	while q:
		v = q.popleft()
		for w in grafo.adyacentes(v):
			if w not in visitados:
				visitados.add(w)
				q.append(w)
				distancia[w] = distancia[v] + 1

	minimo = 0
	for v in distancia:
		if v == y and minimo > distancia[v]:
			minimo = distancia[v]

	return minimo


