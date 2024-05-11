class ListaEnlazada:

    def __init__(self):
        # prim es un _Nodo o None
        self.prim = None
        self.cant = 0

    def suma_acumulativa(self):
        nueva = ListaEnlazada()
        
        act_self = self.prim
        act_nueva = None
        while act_self:
            if act_nueva:
                suma = act_nueva.dato + act_self.dato
                act_nueva.prox = _Nodo(suma)
            else:
                nueva.prim = _Nodo(act_self.dato)
                act_nueva = nueva.prim 
                act_self =act_self.prox
                continue
            act_self = act_self.prox
            act_nueva = act_nueva.prox
        return nueva


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
l2 = l1.suma_acumulativa()
print(l2)
print(l1)