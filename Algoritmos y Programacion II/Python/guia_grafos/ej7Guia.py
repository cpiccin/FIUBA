# Proponer una función para calcular el grafo traspuesto G^T de un grafo dirigido G. El grafo traspuesto G^T
# posee los mismos vértices que G, pero con todas sus aristas invertidas (por cada arista (v, w) en G, 
# existe una arista (w, v) en G^T
# Indicar la complejidad para un grafo implementado con:

# a. lista de adyancencias

# b. matriz de adyacencias

from grafo import Grafo

def grafo_transpuesto(grafo):
  grafo_transpuesto = Grafo(True, grafo.obtener_vertices())
  for v in grafo.obtener_vertices():
    for w in grafo.adyacentes(v):
      grafo_transpuesto.agregar_arista(w, v)
  return grafo_transpuesto


grafo1 = Grafo(True, ["A", "B", "C", "D", "E"])
grafo1.agregar_arista("A", "B")
grafo1.agregar_arista("B", "A")
grafo1.agregar_arista("B", "C")
grafo1.agregar_arista("C", "E")
grafo1.agregar_arista("E", "B")
grafo1.agregar_arista("D", "B")
print(grafo_transpuesto(grafo1))