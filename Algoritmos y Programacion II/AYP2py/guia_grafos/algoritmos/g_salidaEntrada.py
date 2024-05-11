from grafo import Grafo

def calcular_grados(grafo):
	gr_entrada, gr_salida = {}, {}

	for v in grafo.obtener_vertices():
		# inicializo todos los grados en 0
		gr_entrada[v], gr_salida = 0, 0

	for v in grafo.obtener_vertices():
		for w in grafo.adyacentes(v):
			gr_salida[v] = gr_salida[v] + 1
			gr_entrada[w] = gr_entrada[w] + 1

	return gr_entrada, gr_salida