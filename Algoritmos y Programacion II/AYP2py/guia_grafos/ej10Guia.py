# Escribir una función bool es_bipartito(grafo) que dado un grafo no dirigido devuelva true o false 
# de acuerdo a si es bipartito o no. Indicar y justificar el orden del algoritmo. 
# ¿Qué tipo de recorrido utiliza?

from grafo import Grafo
from collections import deque

def es_bipartito(grafo):
    conjuntos = {}
    q = deque()

    origen = grafo.vertice_aleatorio()
    conjuntos[origen] = 0
    q.append(origen)

    # BFS
    while q:
        v = q.popleft() # es desencolar
        for w in grafo.adyacentes(v):
            if w not in conjuntos:
                conjuntos[w] = 1 - conjuntos[v] # va a ser 0 o 1
                q.append(w) # encolar
            if conjuntos[w] == conjuntos[v]:
                return False
    return True


grafo1 = Grafo(False, ["A", "B", "C", "D", "E", "F"])
grafo1.agregar_arista("A", "D")
grafo1.agregar_arista("A", "C")
grafo1.agregar_arista("A", "F")
grafo1.agregar_arista("F", "B")
grafo1.agregar_arista("B", "E")
# grafo1.agregar_arista("D", "C")
print(es_bipartito(grafo1))
