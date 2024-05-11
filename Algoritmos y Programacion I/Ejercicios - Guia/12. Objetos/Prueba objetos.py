def valida_numero(valor):
		if not isinstance(valor, (int, float, complex)):
			raise TypeError(f'{valor!r} no es un numero')
		return valor

class Punto:

	def __init__(self, x, y):
		self.x = valida_numero(x)
		self.y = valida_numero(y)

	def suma(self, p2):
		return (self.x + p2.x, self.x + p2.y)

	def resta(self, p2):
		return Punto(self.x - p2.x, self.x - p2.y)

	def norma(self):
		return (self.x*self.x + self.y*self.y)**0.5

	def distancia(self, p2):
		return self.resta(p2).norma()

	def __str__(self):
		return f'({self.x}, {self.y})'

	def __repr__(self):
		return f'Punto({self.x}, {self.y})'

	def __add__(self, p2):
		return Punto(self.x+p2.x, self.y+p2.y)

	def __sub__(self, p2):
		return Punto(self.x - p2.x, self.y - p2.y)

	def desplazar(self, dx, dy):
		return Punto(self.x + dx, self.y + dy)

