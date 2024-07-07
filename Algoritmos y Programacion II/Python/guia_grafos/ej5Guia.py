# Implementar un algoritmo que, dado un grafo dirigido, nos devuelva un ciclo dentro del mismo, 
# si es que lo tiene. Indicar el orden del algoritmo.

from grafo import Grafo

def obtener_ciclo(grafo):
  visitados = {}
  padre = {}
  for v in grafo.obtener_vertices():
    if v not in visitados:
      ciclo = dfs_ciclo(grafo, v, visitados, padre)
      if ciclo is not None:
        return ciclo
  return None

def dfs_ciclo(grafo, v, visitados, padre):
  visitados[v] = True
  for w in grafo.adyacentes(v):
    if w in visitados:
      if w != padre[v]:
        return reconstruir_ciclo(padre, w, v)
    else:
      padre[w] = v
      ciclo = dfs_ciclo(grafo, w, visitados, padre)
      if ciclo is not None:
        return ciclo
  return None

def reconstruir_ciclo(padre, inicio, fin):
  v = fin
  camino = []
  while v != inicio:
    camino.append(v)
    v = padre[v]
  camino.append(inicio)
  return camino[::-1]


grafo1 = Grafo(False, ["A", "B", "C", "D", "E"])
grafo1.agregar_arista("A", "B")
grafo1.agregar_arista("B", "C")
grafo1.agregar_arista("B", "E")
grafo1.agregar_arista("E", "D")
grafo1.agregar_arista("D", "B")
print(grafo1)
# print(obtener_ciclo(grafo1))