def bfs(grafo):
	visitados = set()
	padre = {}
	orden = {}
	origen = grafo.vertice_aleatorio()
	cola = deque()
	visitados.add(origen)
	cola.append(origen)
	padre[origen] = None
	orden[origen] = 0
	while cola:
		v = cola.popleft()
		for w in grafo.adyacentes(v):
			if w not in visitados:
				visitados.add(v)
				padre[w] = v 
				orden[w] = orden[v]+1
				cola.append(w)
	return orden, padre


def dfs(grafo):
	visitados = set()
	padre = {}
	orden = {}
	for v in grafo.obtener_vertices():
		if v not in visitados:
			padre[v] = None
			orden[v] = 0
			dfs_rec(grafo, v, visitados, padre, orden)
	return padre, orden

def dfs_rec(grafo, v, visitados, padre, orden):
	visitados.add(v)
	for w in grafo.adyacentes(v):
		if w not in visitados:
			padre[w] = v
			orden[w] = orden[v] + 1
			dfs_rec(grafo, w, visitados, padre, orden)


def orden_topologico_radial(grafo):
	orden = {}
	for v in grafo.obtener_vertices():
		orden[v] = 0 
	for v in grafo.obtener_vertices():
		for w in grafo.adyacentes(v):
			orden[w] += 1
	cola = deque()
	res = []
	for v in grafo.obtener_vertices():
		if orden[v] == 0:
			cola.encolar(v)
	while cola:
		v = cola.popleft()
		res.append(v)
		for w in grafo.adyacentes(v):
			orden[w] -= 1
			if orden[w] == 0:
				cola.append(w)

	# identificar ciclo
	if len(res) != len(grafo.obtener_vertices()):
		return None
	return res 


def orden_topologico_dfs(grafo):
	visitados = set()
	pila = deque()
	for v in grafo.obtener_vertices():
		if v not in visitados:
			dfs_topologico(grafo, v, visitados, pila)		
	res = []
	while pila:
		res.append(pila.popright())
	return res

def dfs_topologico(grafo, v, visitados, pila):
	visitados.add(v)
	for w in grafo.adyacentes(v):
		if w not in visitados:
			dfs_topologico(grafo, w, visitados, pila)
	pila.append(v)


def caminos_minimos_dijkstra(grafo, origen):
	q = MinHeap()
	distancia = {}
	for v in grafo.obtener_vertices():
		distancia[v] = math.inf 
	distancia[origen] = 0
	q.encolar(origen, distancia[origen])
	padre = {}
	padre[origen] = None
	while not q.esta_vacia():
		v = q.desencolar()
		for w in grafo.adyacentes(v):
			n = distancia[v] + grafo.peso_arista(v, w)
			if n < distancia[w]:
				distancia[w] = n 
				padre[w] = v 
				q.encolar(w, distancia[w])
	return padre, distancia


def caminos_minimos_bf(grafo, origen):
	distancia = {}
	padre = {}
	for v in grafo.obtener_vertices():
		distancia[v] = math.inf 
	distancia[origen] = 0
	padre[origen] = None 
	aristas = grafo.obtener_aristas()

	for i in range(grafo.obtener_vertices()):
		for v, w, peso in aristas:
			n = distancia[v] + peso
			if n < distancia[w]:
				distancia[w] = n 
				padre[w] = v 
	# identifica ciclos negativos
	for v, w, peso in aristas:
		n = distancia[v] + peso 
		if n < distancia[w]:
			return None 
	return padre, distancia



def mst_prim(grafo):
	q = MinHeap()
	visitados = set()
	origen = grafo.vertice_aleatorio()
	arbol = Grafo(False, grafo.obtener_vertices())
	for w in grafo.adyacentes(origen):
		q.encolar((v, w), grafo.peso_arista(v, w))
	visitados.add(origen)
	while not q.esta_vacia():
		v, w = q.desencolar()
		if w in visitados:
			continue
		arbol.agregar_arista(v, w, grafo.peso_arista(v, w))
		visitados.add(w)
		for ady in grafo.adyacentes(w):
			if ady not in visitados:
				q.encolar((w, ady), grafo.peso_arista(w, ady))
	return arbol


def mst_kruskal(grafo):
	conjuntos = UnionFind(grafo.obtener_vertices())
	q = MinHeap()
	aristas = grafo.obtener_aristas()
	arbol = Grafo(False, grafo.obtener_vertices())
	for arista in aristas:
		q.encolar(arista, arista[2])
	while not q.esta_vacia():
		v, w = q.desencolar()
		if conjuntos.find(v) == conjuntos.find(w):
			continue
		arbol.agregar_arista(v, w, grafo.peso_arista(v, w))
		conjuntos.union(v, w)
	return arbol	



def puntos_articulacion(grafo):
	visitados = set()
	origen = grafo.vertice_aleatorio()
	padre = {origen: None}
	orden = {origen: 0}
	visitados.add(origen)
	mas_bajo = {}
	res = set()
	es_raiz = True
	dfs_puntos_articulacion(grafo, origen, visitados, padre, orden, mas_bajo, res, es_raiz)
	return res 


def dfs_puntos_articulacion(g, v, vis, padre, orden, mas_bajo, res, es_raiz):
	hijos = 0
	mas_bajo[v] = orden[v]
	for w in g.adyacentes(v):
		if w not in vis:
			vis.add(w)
			padre[w] = v 
			orden[w] = orden[v]+1
			dfs_puntos_articulacion(g, w, vis, padre, orden, mas_bajo, res, es_raiz)
			if mas_bajo[w] >= orden[v] and not es_raiz:
				res.add(v)
			mas_bajo[v] = min(mas_bajo[v], mas_bajo[w])
		elif padre[v] != w:
			mas_bajo[v] = min(mas_bajo[v], orden[w])
	if es_raiz and hijos > 1:
		res.add(v)


def cfc(grafo):
	res = []
	visitados = set()
	for v in grafo.obtener_vertices():
		if v not in visitados:
			orden, mas_bajo, apilados = {},{},set()
			pila = crear_pila()
			dfs_cfc(grafo, v, vis, orden, mas_bajo, apilados, pila, [0])
	return res 


def dfs_cfc(grafo, v, visitados, orden, mas_bajo, apilados, pila, contador_global):
	orden[v] = mas_bajo[v] = contador_global[0]
	contador_global[0]+=1
	visitados.add(v)
	apilados.add(v)
	pila.apilar(v)
	for w in grafo.adyacentes(v):
		if w not in visitados:
			dfs_cfc(grafo, w, visitados, orden, mas_bajo, apilados, pila, contador_global)
		if w in apilados:
			mas_bajo[v] = min(mas_bajo[v], mas_bajo[w])

	if orden[v] == mas_bajo[v]:
		nueva_cfc = []
		while True:
			w = pila.desapilar()
			apilados.remove(w)
			nueva_cfc.append(w)
			if v == w:
				break
		res.append(nueva_cfc)