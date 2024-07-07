from collections import deque
from grafo import Grafo


def func(grafo):
	grados = {}

	for v in grafo.obtener_vertices():
		grados[v] = 0

	for v in grafo.obtener_vertices():
		for w in grafo.adyacentes():
			grados[v] += 1

	cant_impares = 0
	for v in grados:
		if grados[v] % 2 != 0:
			cant_impares += 1

	if cant_impares % 2 == 0:
		return True

	return False
