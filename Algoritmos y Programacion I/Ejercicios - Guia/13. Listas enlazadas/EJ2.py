# VER: SI SE EXTIENDE L2 SE MODIFICA L1 

class ListaEnlazada:

    def extend1(self, lista_aux):
        
        if not self.prim:
            self.prim = lista_aux.prim
            self.cant = lista_aux.cant
            return
        
        if not lista_aux.prim:
            return
        
        act_lista_aux = lista_aux.prim
        
        if not act_lista_aux.prox:
            nuevo = _Nodo(act_lista_aux)            
            nuevo.dato = act_lista_aux.dato
            act = self.prim
            while act.prox:
                act = act.prox
            act.prox = nuevo
            self.cant += 1
            return
        
        while lista_aux.prim.prox:
            nuevo = _Nodo(act_lista_aux)
            nuevo.dato = act_lista_aux.dato
            act = self.prim
            while act.prox:
                act = act.prox
            act.prox = nuevo
            if act_lista_aux.prox == None:
                break
            act_lista_aux = act_lista_aux.prox
        
        self.cant += lista_aux.cant
        

    def extend2(self, lista_aux):
        if self.cant == 0 and len(lista_aux) == 0:
            return
        
        aux = lista_aux.prim
        if self.prim is None:
            self.prim = _Nodo(aux.dato)
            act = self.prim
        else:
            act = self.prim
            for i in range(self.cant-1):
                act = act.prox
            if len(lista_aux) == 0:
                return
            act.prox = _Nodo(aux.dato)
            act = act.prox

        for i in range(len(lista_aux)-1):
            act.prox = _Nodo(aux.prox.dato)
            act = act.prox
            aux = aux.prox
        
        self.cant += len(lista_aux)


    def extend(self, otro):
        act_self = self.prim
        while act_self and act_self.prox:
            act_self = act_self.prox
        act_otro = otro.prim
        while act_otro.prox:
            nuevo = _Nodo(act_otro)
            nuevo.dato = act_otro.dato
            act = self.prim
            while act.prox:
                act = act.prox
            act.prox = nuevo
            if act_otro.prox == None:
                break
            act_otro = act_otro.prox


    def extend3(self, otro):
        act_self = self.prim
        while act_self and act_self.prox:
            act_self = act_self.prox
        act_otro = otro.prim
        while act_otro:
            if act_self:
                nuevo = _Nodo(act_otro.dato)
                act_self.prox = nuevo
            if not act_self.prox:
                act_self = _Nodo(act_otro.dato)
                act_self = self.prim
            act_otro = act_otro.prox
            act_self = act_self.prox


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
l1.append(1)
l1.append(2)
l1.append(3)

l2 = ListaEnlazada()
l2.append(4)
l2.append(5)
l2.append(6)

l3 = ListaEnlazada()
l3.append(7)
l3.append(15)

print('l1 original: ', l1)
print('l2 original: ', l2)

l1.extend3(l2)

print('l1 + l2: ', l1)

l2.extend3(l3)

print('l2: ', l2)

print('l1: ', l1)

