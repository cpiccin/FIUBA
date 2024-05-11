class Vector:

	def __init__(self, coord):
		if len(coord) == 0:
			raise ValueError('No hay coordenadas')
		self.coord = coord
		
	def __str__(self):
		return str(self.coord)

	def __add__(self, v2):
		if len(self.coord) != len(v2.coord):
			raise ValueError('No tienen iguales dimensiones')
		suma = []
		for i in range(len(self.coord)):
			suma.append(self.coord[i]+v2.coord[i])
		return Vector(suma)

	def __mul__(self, n):
		mul = []
		for num in self.coord:
			mul.append(num*n)
		return Vector(mul)


v1 = Vector([1,4,2,5])
v2 = Vector([4,34,21,4])
v3 = Vector([3,7,1])

print(v1*2)