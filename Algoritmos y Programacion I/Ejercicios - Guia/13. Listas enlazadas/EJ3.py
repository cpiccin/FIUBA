class ListaEnlazada:

    def remover_todos(self, elem):
        contador = 0
        act = self.prim
        ant = None
        if self.cant == 1 and act.dato == elem:
            self.prim = None
            self.cant = 0
            return 1        
        while act:
            if act.dato == elem:
                if ant:
                    ant.prox = act.prox
                else:
                    self.prim = act.prox
                self.cant -= 1
                act = act.prox
                contador += 1
            else:
                ant = act
                act = act.prox
        return contador


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

class _Nodo:
    def __init__(self, dato, prox=None):
        self.dato = dato
        self.prox = prox




l1 = ListaEnlazada()

l1.append(4)
l1.append(3)
l1.append(5)
l1.append(0)
l1.append(1)
l1.append(3)

print(l1.remover_todos(3))
print(l1)