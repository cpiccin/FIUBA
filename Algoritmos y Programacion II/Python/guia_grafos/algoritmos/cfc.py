from grafo import Grafo
from collections import deque

# Algoritmo de Tarjan. Aplicacion de DFS.
# Se aplica DFS; 


def componentes_fuertemente_conexas(grafo):
    res = []
    visitados, orden, mas_bajo, pila, apilados, contador_global = set(), {}, {}, [], set(), [0]
    for v in grafo.obtener_vertices():
        if v not in visitados:
            dfs_cfc(grafo, v, visitados, orden, mas_bajo, pila, apilados, contador_global, res)
    return res 

def dfs_cfc(grafo, v, visitados, orden, mas_bajo, pila, apilados, cont, res):
    orden[v] = mas_bajo[v] = cont[0]
    print(cont)
    cont[0] += 1
    pila.append(v)
    visitados.add(v)
    apilados.add(v)
    for w in grafo.adyacentes(v):
        print("v: ", v, "  adyacente que estoy viendo: ", w)
        if w not in visitados:
            dfs_cfc(grafo, w, visitados, orden, mas_bajo, pila, apilados, cont, res)
        if w in visitados:
            print("se actualizo el mas_bajo: ", v, w)
            mas_bajo[v] = min(mas_bajo[v], mas_bajo[w])

    if orden[v] == mas_bajo[v]:
        print("V que cierra cfc: ", v)
        nueva_cfc = []
        while True:
            w = pila.pop()
            apilados.remove(w)
            nueva_cfc.append(w)
            if w == v:
                break
        res.append(nueva_cfc)


grafo1 = Grafo(True, ["A", "B", "C", "D", "E", "F", "G"])
grafo1.agregar_arista("A", "C")
grafo1.agregar_arista("C", "F")
grafo1.agregar_arista("F", "D")
grafo1.agregar_arista("D", "C")
grafo1.agregar_arista("C", "B")
grafo1.agregar_arista("G", "B")
grafo1.agregar_arista("B", "E")
grafo1.agregar_arista("E", "G")
print(componentes_fuertemente_conexas(grafo1))