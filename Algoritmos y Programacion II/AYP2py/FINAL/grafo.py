import random

class Grafo:
    def __init__(self, dirigido = False, vertices_iniciales = []):
        self.vertices = {}
        self.dirigido = dirigido
        for vertice in vertices_iniciales:
            self.agregar_vertice(vertice)

    def agregar_vertice(self, v):
        if v not in self.vertices:
            self.vertices[v] = {}

    def borrar_vertice(self, v):
        if v not in self.obtener_vertices():
            return
        del self.vertices[v]
        for vertice in self.vertices:
            if v in self.vertices[vertice]:
                del self.vertices[vertice][v]
        return v 

    def agregar_arista(self, v, w, peso = 1):
        if v in self.vertices and w in self.vertices:
            self.vertices[v][w] = peso 
        if not self.dirigido:
            self.vertices[w][v] = peso 

    def borrar_arista(self, v, w):
        if v in self.vertices and w in self.vertices:
            del self.vertices[v][w]
        if not self.dirigido:
            del self.vertices[w][v]

    def estan_unidos(self, v, w):
        return v in self.vertices and w in self.vertices[v]

    def peso_arista(self, v, w):
        if self.estan_unidos(v, w):
            return self.vertices[v][w]
        return None

    def obtener_vertices(self):
        return list(self.vertices.keys())

    def obtener_aristas(self):
        aristas = []
        for v in self.vertices:
            for w in self.vertices[v]:
                arista = (v, w, self.peso_arista(v, w))
                aristas.append(arista)
        return aristas

    def adyacentes(self, v):
        if v in self.vertices:
            return list(self.vertices[v].keys())
        return []

    def vertice_aleatorio(self):
        return random.choice(self.obtener_vertices())

    def __str__(self):
        res = ""
        for v in self.vertices:
            res += v + ": " + str(self.adyacentes(v)) + "\n"
        return res