class _Nodo:
    def __init__(self, dato, prox=None):
        self.dato = dato
        self.prox = prox


class Cola:

	def __init__(self):
		self.primero = None
		self.ultimo = None

	def __str__(self):
		lista = '['
		act = self.primero
		while act:
			lista += str(act.dato)
			if act.prox:
				lista += ', '
			act = act.prox
		lista += ']'
		return lista

	def encolar(self, x):
		nuevo = _Nodo(x)
		if self.ultimo is not None:
			self.ultimo.prox = nuevo
			self.ultimo = nuevo
		else:
			self.primero = nuevo
			self.ultimo = nuevo

	def desencolar(self):
		if self.primero is None:
			raise ValueError("La cola está vacía")
		valor = self.primero.dato
		self.primero = self.primero.prox
		if not self.primero:
			self.ultimo = None
		return valor


	def esta_vacia(self):
		return self.primero is None


def invierte(cola):
    if cola.esta_vacia():
        return cola
    dato = cola.desencolar()
    invierte(cola)
    cola.encolar(dato)
    
 
def invierte2(cola):
	try:
		n = cola.desencolar()
	except ValueError:
		return
	invierte2(cola)
	cola.encolar(n)



c1 = Cola()
c1.encolar(1)
c1.encolar(2)
c1.encolar(3)
c1.encolar(4)
print(c1)
invierte(c1)
print(c1)