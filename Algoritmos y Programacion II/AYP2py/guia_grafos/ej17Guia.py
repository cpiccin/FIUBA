# Implementar una función que reciba un grafo no dirigido, y que compruebe la siguiente afirmación: 
# “La cantidad de vértices de grado IMPAR es PAR”. Indicar y justificar el orden del algoritmo si el
# grafo está implementado como matriz de adyacencia.


from grafo import Grafo

def comprueba(grafo):
	grados = {}
	
	for v in grafo.obtener_vertices():
		if v not in grados:
			grados[v] = 0
		for w in grafo.adyacentes(v):
			grados[v] += 1

	cant_g_impar = 0
	for g in grados:
		if grados[g] % 2 != 0:
			cant_g_impar += 1

	if cant_g_impar % 2 == 0:
		return True
	return False


grafo1 = Grafo(False, ["A", "B", "C", "D", "E", "F", "G"])
grafo1.agregar_arista("A", "B")
grafo1.agregar_arista("B", "E")
grafo1.agregar_arista("B", "C")
grafo1.agregar_arista("D", "B")
grafo1.agregar_arista("E", "D")
print(comprueba(grafo1))