class ListaEnlazada:

    def invertir(self):
        ant = None
        act = self.prim
        while act:
            sig = act.prox
            act.prox = ant
            ant = act
            act = sig
        self.prim = ant

    def invertir_con_pila(self):
        pila = Pila()
        act = self.prim
        while act:
            pila.apilar(act.dato)
            act = act.prox
        act = self.prim
        while act:
            act.dato = pila.desapilar()
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