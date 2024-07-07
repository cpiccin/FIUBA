from grafo import Grafo

def calcular_grados(grafo):
	gr_entrada, gr_salida = {}, {}

	for v in grafo.obtener_vertices():
		# inicializo todos los grados en 0
		gr_entrada[v], gr_salida = 0, 0

	for v in grafo.obtener_vertices():
		for w in grafo.adyacentes(v):
			gr_salida[v] += 1
			gr_entrada[w] += 1

	return gr_entrada, gr_salida


def ecosistema(grafo):
	g_e, g_s = calcular_grados(grafo)
	res = set()
	for v in grafo.obtener_vertices():
		for w in grafo.adyacentes(v):
			if g_e[w] == 1: # v es lo unico que se come a w
				res.add(v)
			if g_s[v] == 1: # w es lo unico que alimenta a v
				res.add(w)
	return res 