from Pila import Pila

class ListaEnlazada:

    def __init__(self):
        # prim es un _Nodo o None
        self.prim = None
        self.cant = 0

    def invertir_con_pila(self):
        pila = Pila()
        act = self.prim
        while act:
            pila.apilar(act.dato)
            act = act.prox
        self.prim = _Nodo(pila.desapilar())
        act_nuevo = self.prim
        while not pila.esta_vacia():
            act_nuevo.prox = _Nodo(pila.desapilar())
            act_nuevo = act_nuevo.prox

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
print(l1)
l1.invertir_con_pila()
print(l1)