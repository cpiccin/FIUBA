

class Caramelera:

	def __init__(self, max_cantidad):
		self.capacidad = max_cantidad
		self.actual = 0
		
	
	def __str__(self):
		return f'Caramelera con {self.actual}/{self.capacidad} caramelos'

	
	def poner_caramelos(self, cantidad):
		if cantidad + self.actual > self.capacidad:	
			raise Exception('No hay lugar')
		self.actual += cantidad


	def sacar_caramelos(self, cantidad):
		if self.actual - cantidad < 0:
			raise Exception('No hay suficientes caramelos')
		self.actual -= cantidad

	
c = Caramelera(20)          
c.poner_caramelos(10)     
c.sacar_caramelos(4)        
print(c.actual)                            
print(c)                    

                        