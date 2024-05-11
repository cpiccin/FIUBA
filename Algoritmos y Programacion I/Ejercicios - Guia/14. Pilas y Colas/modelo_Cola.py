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


	def esta_vacia(self):
		return self.primero is None

