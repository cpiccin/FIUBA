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
        
    def borrarUltimo(self):
        ant = None
        act = self.prim
        while act.prox:
            ant = act
            act = act.prox 
        ant.prox = None

        
class _Nodo:
    def __init__(self, dato, prox=None):
        self.dato = dato
        self.prox = prox
        
        
        
l1 = ListaEnlazada()
l1.append(1)
l1.append(2)
l1.append(3)
l1.append(4)
print(l1)
l1.borrarUltimo()
print(l1)