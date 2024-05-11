from grafo import Grafo
from collections import deque

# Algoritmo de Tarjan. Aplicacion de DFS.
# Se aplica DFS; 


def dfs_cfc(grafo, v, visitados, orden, mas_bajo, pila, apilados, cfcs, contador_global):
    orden[v] = mas_bajo[v] = contador_global[0]
    contador_global[0] += 1
    visitados.add(v)
    pila.apilar(v)
    apilados.add(v)
    for w in grafo.adyacentes(v):
        if w not in visitados:
            # llamamos recursivamente
            dfs_cfc(grafo, w, visitados, orden, mas_bajo, pila, apilados, cfcs, contador_global)
        if w in apilados:
            # Nos tenemos que fijar que este entre los apilados y que no estemos viendo a un vertice visitado
            # en otro dfs hecho antes --> no son parte de la misma CFC porque habrian sido visitados en el mismo DFS
            mas_bajo[v] = min(mas_bajo[v], mas_bajo[w])
 
    if orden[v] == mas_bajo[v]:
        # Se cumple condicion de cierre de CFC, armamos
        nueva_cfc = []
        while True: # porque python no tiene un do-while
            w = pila.desapilar()
            apilados.remove(w)
            nueva_cfc.append(w)
            if w == v:
                break
        cfcs.append(nueva_cfc)
 
 
def cfcs_grafo(grafo):
    resultados = []
    visitados = set()
    for v in grafo:
        if v not in visitados:
            dfs_cfc(grafo, v, visitados, {}, {}, Pila(), set(), resultados, [0])
    return resultados