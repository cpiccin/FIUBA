class Nodo:

	def __init__(self, dato=None, prox=None):
		self.dato = dato
		self.prox = prox

	def __str__(self):
		return str(self.dato)


n1 = Nodo('Bananas')
n2 = Nodo('Peras', n1)
n3 = Nodo('Manzanas', n2)

print(n1, n2, n3)