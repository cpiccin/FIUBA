class ListaEnlazada:

    def filter(self, f):
        nueva_lista = ListaEnlazada()
        act = self.prim
        act_nueva = None
        while act:
            if f(act.dato):
                if not act_nueva:
                   nueva_lista.prim = _Nodo(act.dato)
                   act_nueva = nueva_lista.prim
                   nueva_lista.cant = 1
                else:
                    act_nueva.prox = _Nodo(act.dato)
                    act_nueva = act_nueva.prox
                    nueva_lista.cant += 1
            act = act.prox
        return nueva_lista



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