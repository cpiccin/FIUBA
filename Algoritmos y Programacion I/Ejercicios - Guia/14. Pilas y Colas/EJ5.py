from modelo_Pila import Pila

class PilaConMaximo:
	def __init__(self):
		self.tope = None
		self.elementos = Pila()
		self.maximo = Pila()

	def apilar(self, dato):
		nodo = _Nodo(dato, self.tope)
		self.elementos.apilar(nodo)
		self.tope = nodo

	def desapilar(self):
		if self.esta_vacia():
			raise ValueError("pila vacía")
		dato = self.tope.dato
		self.tope = self.tope.prox
		self.elementos.desapilar()
		return dato

	def ver_tope(self):
		if self.esta_vacia():
			raise ValueError("pila vacía")
		return self.tope.dato

	def esta_vacia(self):
		return self.tope is None

	def obtener_maximo(self):
		maxi = 0
		if self.tope.dato > maxi:
			maxi = self.tope.dato
			self.maximo.apilar(maxi)
			self.elementos.desapilar()
			return self.maximo.tope.dato
		else:
			return self.maximo.tope.dato



class _Nodo:
	def __init__(self, dato, prox=None):
		self.dato = dato
		self.prox = prox


p = PilaConMaximo()
p.apilar(3)
print(p.obtener_maximo())

p.apilar(6)
print(p.obtener_maximo())

p.ver_tope()

p.apilar(2)
print(p.obtener_maximo())