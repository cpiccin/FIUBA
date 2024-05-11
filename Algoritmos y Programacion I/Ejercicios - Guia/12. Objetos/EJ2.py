def valida_numeros(n):
	if n == 0:
		raise ZeroDivisionError('No se puede dividir por 0')
	return n 

def euclides(m, n):
	while True: 
		resto = m % n
		if resto == 0: # se repite el ciclo hasta que el resto es 0
			return n
		m = n 
		n = resto

class Fraccion:

	def __init__(self, dividendo, divisor):
		self.x = dividendo
		self.y = valida_numeros(divisor)

	def __str__(self):
		return f'{self.x}/{self.y}'

	def __add__(self, f2):
		if self.y == f2.y:
			return Fraccion(self.x+f2.x, self.y).simplificar()
		return Fraccion(f2.y*self.x+f2.x*self.y, self.y*f2.y).simplificar()

	def __mul__(self, f2):
		return Fraccion(self.x*f2.x, self.y*f2.y).simplificar()

	def simplificar(self):
		mcm = euclides(self.x, self.y)
		self.x = int(self.x/mcm)
		self.y = int(self.y/mcm)
		return self



f1 = Fraccion(2,5)
f2 = Fraccion(13,5)
print(type(f1))
print(f1+f2)
