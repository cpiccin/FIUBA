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

    def clonar(self):
        nueva_lista = ListaEnlazada()
        act = self.prim
        nueva_lista.prim = _Nodo(self.prim.dato)
        nueva_lista.cant = 1
        act_nueva = nueva_lista.prim
        while act.prox:
            nueva_lista.cant += 1
            nuevo_nodo = _Nodo(act.prox.dato)
            act = act.prox
            act_nueva.prox = nuevo_nodo
            act_nueva = act_nueva.prox
        return nueva_lista
                
               
        
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
L.clonar()