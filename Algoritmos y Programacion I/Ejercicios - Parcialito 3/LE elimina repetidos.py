class _Nodo:

    def __init__(self, dato=None, prox=None):
        self.dato = dato
        self.prox = prox

class ListaEnlazada:

    def __init__(self):
        self.prim = None
        self.len = 0

    def append(self, x):
        nuevo = _Nodo(x)
        if self.prim == None:
            self.prim = nuevo
            self.len = 1
        else:
            act = self.prim
            while act.prox:
                act = act.prox
            act.prox = nuevo
            self.len += 1

    def __len__(self):
        cont = 0
        act = self.prim
        while act:
            act = act.prox
            cont += 1
        return cont

    def elimina_repetidos(self):
        act = self.prim
        dato_ant = None
        while act:
            if dato_ant == None or act.dato > dato_ant.dato:
                dato_ant = act
            if act.dato == dato_ant.dato:
                dato_ant.prox = act.prox
            act = act.prox
               
        
L = ListaEnlazada()
L.append(1)
L.append(2)
L.append(3)
L.append(3)
L.append(3)
L.append(5)
L.append(7)
L.append(7)
L.append(8)
L.elimina_repetidos()