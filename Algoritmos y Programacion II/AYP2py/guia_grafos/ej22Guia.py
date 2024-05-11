# Implementar una función que reciba un grafo no dirigido y determine si el mismo no tiene ciclos de una cantidad impar de vértices. 
# Indicar y justificar la complejidad de la función.

from grafo import Grafo

def tiene_ciclos_impar(grafo):
	visitados = {}
	padre = {}
	ciclo = obtener_ciclo(grafo, visitados, padre)
	if ciclo == None or len(ciclo) % 2 != 0:
		return False
	return True # el ciclo tiene cantidad par de vertices

def obtener_ciclo(grafo, visitados, padre):
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

grafo1 = Grafo(False, ["A", "B", "C", "D", "E", "F"])
grafo1.agregar_arista("A", "B")
grafo1.agregar_arista("B", "C")
grafo1.agregar_arista("B", "E")
grafo1.agregar_arista("D", "F")
grafo1.agregar_arista("E", "F")
grafo1.agregar_arista("D", "B")
print(tiene_ciclos_impar(grafo1))