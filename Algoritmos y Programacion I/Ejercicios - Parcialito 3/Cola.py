class _Nodo:
    def __init__(self, dato, prox=None):
        self.dato = dato
        self.prox = prox


class Cola:

	def __init__(self):
		self.primero = None
		self.ultimo = None


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

	def __str__(self):
		res = 'sale < '
		act = self.primero
		while act:
			res += str(act.dato) + ' '
			act = act.prox
		return res + '< entra'

	def esta_vacia(self):
		return self.primero is None

# c1 = Cola()
# c1.encolar(1)
# c1.encolar(2)
# c1.encolar(3)
# c1.encolar(4)
# print(c1)

# act = c1.primero
# sig = act.prox

# print(act.dato, sig.dato)
# sig = act
# act = act.prox
# print(act.dato, sig.dato) 