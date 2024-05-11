class Botella:

	def __init__(self, capacidad):
		self.capacidad = capacidad
		self.cantidad = 0 


	def __str__(self):
		return f'Botella: {self.cantidad}/{self.capacidad}cc'


	def esta_vacia(self):
		if self.cantidad == 0:
			return True
		return False


	def cargar(self, carga):
		if (self.cantidad + carga) > self.capacidad:
			raise Exception('La botella no cuenta con capacidad suficiente')
		self.cantidad += carga


	def servir(self, carga):
		if carga > self.cantidad:
			raise Exception('La botella no cuenta con carga suficiente')
		self.cantidad -= carga 
		


botella = Botella(750)

print(botella)
print(botella.esta_vacia())	
botella.cargar(500)
print(botella)
botella.servir(499)
print(botella)
botella.cargar(1000)