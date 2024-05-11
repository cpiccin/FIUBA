class ListaEnlazada:

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

    def __str__(self):
        lista = '['
        act = self.prim
        while act:
            lista += str(act.dato)
            if act.prox:
                lista += ', '
            act = act.prox
        lista += ']'
        return lista
        
    def slice(self, i, f):
        nueva = ListaEnlazada()

        act_self = self.prim
        
        for _ in range(i):
            act_self = act_self.prox
        
        nueva.prim = _Nodo(act_self.dato)
        act_nueva = nueva.prim

        for _ in range(f-i-1):
            act_self = act_self.prox
            act_nueva.prox = _Nodo(act_self.dato)
            act_nueva = act_nueva.prox
        
        if act_nueva.prox:
            act_nueva.prox = None
        
        return nueva

class _Nodo:
    def __init__(self, dato, prox=None):
        self.dato = dato
        self.prox = prox
        
        
        
l1 = ListaEnlazada()
l1.append(1)
l1.append(2)
l1.append(3)
l1.append(4)
l1.append(5)
l1.append(6)
print(l1)
l2 = l1.slice(1, 3)
print(l2)
print(l1) # NO SE MODIFICA L1 =)