# a) 

def valida_desde_menor_hasta(desde, hasta):
	if desde > hasta:
		raise SyntaxError('El tiempo inicial no puede ser mayor que el final.')
	return desde, hasta

class Intervalo:

	def __init__(self, desde, hasta):
		self.desde, self.hasta = valida_desde_menor_hasta(desde, hasta)

	def duracion(self):
		return (self.hasta - self.desde)

	def interseccion(self, i2):
		inicio = 0
		final = 0
		if self.hasta <= i2.hasta and self.hasta >= i2.desde:
			final = self.hasta
		if i2.hasta <= self.hasta and i2.hasta >= self.desde:
			final = i2.hasta
		if self.desde >= i2.desde and self.desde <= final:
			inicio = self.desde
		if i2.desde >= self.desde and i2.desde <= final:
			inicio = i2.desde
		else:
			raise print('No existe interseccion entre los intervalos.')
		return Intervalo(inicio, final)

	def union(self, i2):
		mayor = 0
		menor = 0
		if self.hasta <= i2.hasta:
			mayor = i2.hasta
		if self.hasta >= i2.hasta:
			mayor = self.hasta
		if self.desde >= i2.hasta:
			menor = i2.desde
		if self.desde <= i2.hasta:
			menor = self.desde
		else:
			raise print('No es posible la union de los intervalos.')
		return Intervalo(menor, mayor)
