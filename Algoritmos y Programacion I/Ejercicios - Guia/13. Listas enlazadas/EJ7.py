class ListaCircular:

    def append(self, dato):
        act = self.prim
        if not act:
            self.prim = _Nodo(dato)
            self.prim.prox = self.prim
            self.cant = 1
            return
        if self.cant > 1:
            for _ in range(self.cant-1):
                act = act.prox
        nuevo = _Nodo(dato)
        act.prox = nuevo
        nuevo.prox = self.prim
        self.cant += 1
        return

    def __len__(self):
        return self.cant

    def __init__(self):
        # prim es un _Nodo o None
        self.prim = None
        self.cant = 0


class _Nodo:
    def __init__(self, dato, prox=None):
        self.dato = dato
        self.prox = prox

l1 = ListaCircular()
l1.append(1)
l1.append(2)
l1.append(3)

print(l1)