# Contamos con un grafo dirigido que modela un ecosistema. 
# En dicho grafo, cada vértice es una especie, y cada arista (v, w) indica que v es depredador natural de w

# Nos puede interesar es saber si existe alguna especie que, si llegara a desaparecer, rompería todo el ecosistema: 
# quienes la depredan no tienen un sustituto (y, por ende, pueden desaparecer también) y/o quienes eran depredados 
# por esta ya no tienen amenazas, por lo que crecerán descontroladamente. 

# Implementar un algoritmo que reciba un grafo de dichas características y devuelva una lista de todas las especies 
# que cumplan lo antes mencionado.

from grafo import Grafo

def ecosistema(grafo):
    origen = grafo.vertice_aleatorio()
    for v in grafo.obtener_vertices():
    	for w in grafo.adyacentes(v):
    		grafo.agregar_arista(w, v)
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



ecosistema_grafo = Grafo(True, ["Leon", "Cebra", "Tigre", "Gacela", "Hiena", "Cocodrilo", "Bufalo", "Elefante", "Jirafa", "Pasto"])
ecosistema_grafo.agregar_arista("Leon", "Cebra")
ecosistema_grafo.agregar_arista("Tigre", "Cebra")
ecosistema_grafo.agregar_arista("Cocodrilo", "Cebra")
ecosistema_grafo.agregar_arista("Leon", "Gacela")
ecosistema_grafo.agregar_arista("Tigre", "Gacela")
ecosistema_grafo.agregar_arista("Hiena", "Gacela")
ecosistema_grafo.agregar_arista("Leon", "Bufalo")
ecosistema_grafo.agregar_arista("Tigre", "Elefante")
ecosistema_grafo.agregar_arista("Hiena", "Cebra")
ecosistema_grafo.agregar_arista("Bufalo", "Pasto")
ecosistema_grafo.agregar_arista("Cocodrilo", "Leon")
ecosistema_grafo.agregar_arista("Cocodrilo", "Cebra")
ecosistema_grafo.agregar_arista("Gacela", "Pasto")
ecosistema_grafo.agregar_arista("Elefante", "Pasto")
ecosistema_grafo.agregar_arista("Jirafa", "Pasto")
ecosistema_grafo.agregar_arista("Cebra", "Pasto")
print(ecosistema(ecosistema_grafo))