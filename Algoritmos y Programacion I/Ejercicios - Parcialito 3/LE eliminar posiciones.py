class _Nodo:

    def __init__(self, dato=None, prox=None):
        self.dato = dato
        self.prox = prox

class ListaEnlazada:

    def __init__(self):
        self.prim = None
        self.cant = 0

    def append(self, x):
        nuevo = _Nodo(x)
        if self.prim == None:
            self.prim = nuevo
            self.cant = 1
        else:
            act = self.prim
            while act.prox:
                act = act.prox
            act.prox = nuevo
            self.cant += 1

    def __len__(self):
        cont = 0
        act = self.prim
        while act:
            act = act.prox
            cont += 1
        return cont

    def eliminar_posiciones(self, sec):
        ant = None
        act = self.prim
        for i in range(sec[len(sec)-1]+1):
            if act == None:
                raise IndexError
            if i==0 and sec[0] == 0:
                self.prim = act.prox
                act = self.prim
                continue
            if i in sec:
                ant.prox = act.prox
                act = act.prox
            else:
                ant = act
                act = act.prox
        
L = ListaEnlazada()
L.append('a')
L.append('c')
L.append('e')
L.eliminar_posiciones((0, 3))