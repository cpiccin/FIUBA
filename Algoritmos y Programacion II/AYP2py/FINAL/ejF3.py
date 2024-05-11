# Implementar un algoritmo que reciba un Grafo con características de árbol (no árbol binario, sino referido a árbol
# de teoría de grafos) y devuelva una lista con los puntos de articulación de dicho árbol. Indicar y justificar la complejidad
# del algoritmo implementado. Importante: aprovechar las características del grafo que se recibe para que la solución sea
# lo más simple posible.

from grafo import Grafo

def ptos_art_arbol(grafo):
	hijos = {}
	res = []
	for v in grafo.obtener_vertices():
		hijos[v] = len(grafo.adyacentes(v))
	for v in hijos:
		if hijos[v] > 0:
			res.append(v)
	return res