class ListaEnlazada:

    def duplicar(self, elem):
        act = self.prim
        while act:
            if act.dato == elem:
                nuevo = _Nodo(elem)
                nuevo.prox = act.prox
                act.prox = nuevo
                act = act.prox.prox
                self.cant += 1
                continue
            act = act.prox

    def __init__(self):
        # prim es un _Nodo o None
        self.prim = None
        self.cant = 0

    def append(self, dato):
        nuevo = _Nodo(dato)
        if not self.prim:
            self.prim = nuevo
        else:
            act = self.prim
            while act.prox:
                act = act.prox
            # act es el ultimo nodo
            act.prox = nuevo
        self.cant += 1

    def __len__(self):
        return self.cant

class _Nodo:
    def __init__(self, dato, prox=None):
        self.dato = dato
        self.prox = prox