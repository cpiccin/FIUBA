from grafo import Grafo
from collections import deque

# Algoritmo de Tarjan. Aplicacion de DFS.
# Variante de DFS para identificar puntos de articulacion en un grafo NO dirigido. Un vertice es un punto de articulacion si:
# 	- V es la raiz del arbol que resulta del DFS y tiene minimo 2 hijos
#	- V no es raiz y alguno de sus hijos no tiene forma de volver a los que sean superiores a V. 
#	No tiene aristas de retorno.

def puntos_articulacion(grafo):
    res = set()
    origen = "G"
    visitados, padre, orden, mas_bajo, es_raiz = set(), {origen:None}, {origen:0}, {}, True
    visitados.add(origen)
    dfs_ptos_art(grafo, origen, padre, orden, visitados, mas_bajo, res, es_raiz)
    return res  

def dfs_ptos_art(grafo, v, padre, orden, visitados, mas_bajo, res, es_raiz):
    mas_bajo[v] = orden[v]
    hijos = 0
    for w in grafo.adyacentes(v):
        print("adyacente: ", w, " de ", v)
        if w not in visitados:
            hijos += 1
            visitados.add(w)
            padre[w] = v 
            orden[w] = orden[v] + 1
            print("entra en recursion el par: ", v, w)
            dfs_ptos_art(grafo, w, padre, orden, visitados, mas_bajo, res, es_raiz=False)
            print("vuelve de la recursion el par: ", v, w)
            if mas_bajo[w] >= orden[v] and not es_raiz:
                print("es pto art: ", v)
                res.add(v)
            mas_bajo[v] = min(mas_bajo[v], mas_bajo[w])
        elif padre[v] != w:
            print("se actualizo el mas_bajo de: ", v)
            mas_bajo[v] = min(mas_bajo[v], orden[w])
    if es_raiz and hijos > 1:
        res.add(v)  


def min(n1, n2):
	if n1 < n2:
		return n1
	return n2
 
grafo1 = Grafo(False, ["A", "B", "C", "D", "E", "F", "G", "H"])
grafo1.agregar_arista("G", "A")
grafo1.agregar_arista("A", "E")
grafo1.agregar_arista("B", "A")
grafo1.agregar_arista("A", "F")
grafo1.agregar_arista("E", "B")
grafo1.agregar_arista("B", "F")
grafo1.agregar_arista("B", "C")
grafo1.agregar_arista("B", "D")
grafo1.agregar_arista("C", "D")
grafo1.agregar_arista("D", "H")
print(puntos_articulacion(grafo1))