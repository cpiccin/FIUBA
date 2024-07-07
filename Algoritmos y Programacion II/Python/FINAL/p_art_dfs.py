from grafo import Grafo
from collections import deque

# Algoritmo de Tarjan. Aplicacion de DFS.
# Variante de DFS para identificar puntos de articulacion en un grafo NO dirigido. Un vertice es un punto de articulacion si:
# 	- V es la raiz del arbol que resulta del DFS y tiene minimo 2 hijos
#	- V no es raiz y alguno de sus hijos no tiene forma de volver a los que sean superiores a V. 
#	No tiene aristas de retorno.

def puntos_articulacion(grafo):
    origen = grafo.random()
    puntos_articulacion = set()
    dfs_puntos_articulacion(grafo, origen, {origen}, {origen: None}, {origen: 0}, {}, puntos_articulacion, True)
    return puntos_articulacion


def dfs_puntos_articulacion(grafo, v, visitados, padre, orden, mas_bajo, ptos, es_raiz):
    hijos = 0
    mas_bajo[v] = orden[v]
    for w in grafo.adyacentes(v):
        if w not in visitados:
            hijos += 1
            orden[w] = orden[v] + 1
            padre[w] = v
            visitados.add(w)
            dfs_puntos_articulacion(grafo, w, visitados, padre, orden, mas_bajo, ptos, es_raiz=False)
            # Lo siguiente se ejecuta una vez ya aplicado a W, y recursivamente a sus hijos
            # Aca se esta en los mas profundo del DFS en esa "rama"
            if mas_bajo[w] >= orden[v] and not es_raiz and v not in ptos:
                # No hubo forma de pasar por arriba a este vertice, es punto de articulacion
                ptos.add(v)
            # Al volver me quedo con que puedo ir tan arriba como mi hijo, si es que me supera
            mas_bajo[v] = min(mas_bajo[v], mas_bajo[w])
        elif padre[v] != w: # evitamos considerar a la arista con el padre como una de retorno
            # Si es uno ya visitado, significa que puedo subir (si es que no podia ya ir mas arriba)
            mas_bajo[v] = min(mas_bajo[v], orden[w])
    # Se volvio en la recursion y se terminaron de ver los adyacentes al modulo
    if es_raiz and hijos > 1:
        ptos.add(v)


def min(n1, n2):
	if n1 < n2:
		return n1
	return n2
 
grafo1 = Grafo(False, ["A", "B", "C", "D", "E", "F", "G"])
grafo1.agregar_arista("A", "B")
grafo1.agregar_arista("A", "F")
grafo1.agregar_arista("B", "C")
grafo1.agregar_arista("B", "E")
grafo1.agregar_arista("C", "D")
grafo1.agregar_arista("C", "E")
grafo1.agregar_arista("C", "G")
grafo1.agregar_arista("E", "G")
grafo1.agregar_arista("D", "E")
print(puntos_articulacion(grafo1))