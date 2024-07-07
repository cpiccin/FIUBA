import random

class Grafo:
    def __init__(self, dirigido, vertices_iniciales=[]):
        self.vertices = {}
        self.dirigido = dirigido
        
        for v in vertices_iniciales:
            self.agregar_vertice(v)
    
    def agregar_vertice(self, v):
        if v not in self.vertices:
            self.vertices[v] = {}
    
    def borrar_vertice(self, v):
        if v in self.vertices:
            del self.vertices[v]
            
            # Eliminar aristas adyacentes
            for vertice in self.vertices:
                if v in self.vertices[vertice]:
                    del self.vertices[vertice][v]
    
    def agregar_arista(self, v, w, p=1):
        if v in self.vertices and w in self.vertices:
            self.vertices[v][w] = p
            
            if not self.dirigido:
                self.vertices[w][v] = p
    
    def borrar_arista(self, v, w):
        if v in self.vertices and w in self.vertices[v]:
            del self.vertices[v][w]
            
            if not self.dirigido:
                del self.vertices[w][v]
    
    def estan_unidos(self, v, w):
        return v in self.vertices and w in self.vertices[v]
    
    def peso_arista(self, v, w):
        if v in self.vertices and w in self.vertices[v]:
            return self.vertices[v][w]
        else:
            return None
    
    def obtener_vertices(self):
        return list(self.vertices.keys())

    def obtener_aristas(self):
        aristas = []
        for v in self.vertices:
            for w in self.vertices[v]:
                arista = (v, w, self.peso_arista(v, w))
                if not self.dirigido and (w, v, self.peso_arista(w, v)) not in aristas:
                    aristas.append(arista)
                elif self.dirigido:
                    aristas.append(arista)
        return aristas
    
    def vertice_aleatorio(self):
        return random.choice(self.obtener_vertices())
    
    def adyacentes(self, v):
        if v in self.vertices:
            return list(self.vertices[v].keys())
        else:
            return []
    
    def __str__(self):
        res = ""
        for v in self.vertices:
            res += v + ": " + str(self.adyacentes(v)) + "\n"
        return res

