class _Nodo:

	def __init__(self, dato=None, prox=None):
		self.dato = dato
		self.prox = prox

	def __str__(self):
		return str(self.dato)


def ver_lista(nodo):
	while nodo is not None:
		print(nodo)
		nodo = nodo.prox


# ------------------------------------------------


class ListaEnlazada:

    def __init__(self):
        self.prim = None
        self.len = 0

    def append(self, x):
        nuevo = _Nodo(x)
        if self.prim == None:
            self.prim = nuevo
            self.len = 1
        else:
            act = self.prim
            while act.prox:
                act = act.prox
            act.prox = nuevo
            self.len += 1

    def __len__(self):
        cont = 0
        act = self.prim
        while act:
        	act = act.prox
        	cont += 1
        return cont
            
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

    def remove(self, x):
        act = self.prim
        ant = None
        while act:
          if act.dato == x:
            if ant: # no se está eliminando el primero
              ant.prox = act.prox
            else:
              self.prim = act.prox
            return
          ant = act
          act = act.prox
    	
L = ListaEnlazada()
L.append(15)
L.append(3)
L.append(-1)
L.append(43)
print(len(L), L.len)
print(L)