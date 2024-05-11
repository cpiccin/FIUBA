class Materia:

	def __init__(self, codigo, nombre, creditos):
		self.codigo = codigo
		self.nombre = nombre
		self.creditos = creditos
		self.materia = [self.codigo, self.nombre, self.creditos] 

class Carrera:

	def __init__(self, materias):
		self.materias = materias # almacena una lista de materias que se tiene que manipular si se aprueba
		self.aprobadas = [] # almacena las materias aprobadas
	
	def __str__(self):
		materias = []
		for i in range(len(self.materias)):
			materias.append([self.materias[i].codigo, self.materias[i].nombre, self.materias[i].creditos])
		return str(materias)

	def aprobar(self, codigo, nota):
		for i in range(len(self.materias)):
			if codigo == self.materias[i].codigo:
				return self.aprobadas.append([codigo, self.materias[i].nombre, nota])
		raise ValueError(f'La materia {codigo} no es parte del plan de estudios')
		
	
	def promedio(self):
		if len(self.aprobadas) == 0:
			raise ValueError('No hay materias aprobadas')
		cantidad = len(self.aprobadas)
		notas = 0
		for i in range(cantidad):
			notas += self.aprobadas[i][2]
		return notas/cantidad

	def materias_aprobadas(self):
		aprobadas = []
		if len(self.aprobadas) == 0:
			return aprobadas
		for materia in self.aprobadas:
			aprobadas.append(f'{materia[0]} {materia[1]} ({materia[2]})')
		return aprobadas

	def creditos_obtenidos(self):
		creditos_totales = 0
		for i in range(len(self.materias)):
			for materia in self.aprobadas:
				if materia[0] == self.materias[i].codigo:
					creditos_totales += self.materias[i].creditos
		return creditos_totales


analisis2 = Materia('61.03', 'Analisis 2', 8)
fisica2 = Materia('62.01', 'Fisica 2', 8)
algo1 = Materia('75.40', 'Algoritmos 1', 6)
c = Carrera([analisis2, fisica2, algo1])

c.aprobar('62.01', 8)
c.aprobar('75.40', 10)
print(c.materias_aprobadas())
print(c.promedio())
print(c.creditos_obtenidos())