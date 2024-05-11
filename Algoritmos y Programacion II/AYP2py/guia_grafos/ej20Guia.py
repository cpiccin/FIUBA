# Implementar un algoritmo que reciba un grafo dirigido y nos devuelva la cantidad de componentes débilmente conexas 
# de este. Indicar y justificar la complejidad del algoritmo implementado.


from grafo import Grafo

# Por cada DFS hay una componente que se recorre.

def comp_debil_conexas(grafo):
    visitados = set()
    cont = 0

    for v in grafo.obtener_vertices():
        for w in grafo.adyacentes(v):
            grafo.agregar_arista(w, v)
            
    for v in grafo.obtener_vertices():
        if v not in visitados:
            dfs(grafo, v, visitados)
            cont += 1
    return cont 

def dfs(grafo, v, visitados):
    visitados.add(v)
    for w in grafo.adyacentes(v):
        if w not in visitados:
            dfs(grafo, w, visitados)


grafo1 = Grafo(True, ["A", "B", "C", "D"])
grafo1.agregar_arista("A", "B")
grafo1.agregar_arista("C", "A")
grafo1.agregar_arista("C", "D")
grafo1.agregar_arista("E", "D")
grafo1.agregar_arista("E", "C")
print(comp_debil_conexas(grafo1))