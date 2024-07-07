# Un árbol es un grafo no dirigido que cumple con las siguientes propiedades:

# a) ||E|| = ||V|| - 1
# b) es aciclico
# c) es conexo 

# Por teorema, si un grafo cumple dos de estas tres condiciones, será árbol (y por consiguiente, cumplirá la tercera). 
# Haciendo uso de ésto (y únicamente de ésto), se pide implementar una función que reciba un grafo no dirigido y 
# determine si se trata de un árbol, o no. Indicar el orden de la función implementada.


from grafo import Grafo
from ej5Guia import obtener_ciclo

def es_arbol(grafo):
	cant_aristas = 0
	visitados = set()
	
	if obtener_ciclo(grafo) != None: # esta operacion es O(V+E)
		return False

	# cuento cantidad de aristas
	for v in grafo.obtener_vertices():
		for w in grafo.adyacentes(v):
			if w not in visitados:
				cant_aristas += 1 
		visitados.add(v)

	if cant_aristas != (len(grafo.obtener_vertices())-1) :
		return False
	return True

# Es O(V+E) + O(V+E) = O(V+E)

grafo1 = Grafo(False, ["A", "B", "C", "D", "E", "F", "G"])
grafo1.agregar_arista("A", "B")
grafo1.agregar_arista("A", "C")
grafo1.agregar_arista("B", "D")
# grafo1.agregar_arista("C", "B")
grafo1.agregar_arista("B", "E")
grafo1.agregar_arista("C", "F")
grafo1.agregar_arista("F", "G")
print(es_arbol(grafo1))
