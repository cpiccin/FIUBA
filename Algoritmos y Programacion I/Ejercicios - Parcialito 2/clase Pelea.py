def valida_entrada(n1, n2):
	try:
		n1 = int(n1)
		n2 = int(n2)
		if n1 < 0 or n2 < 0:
			raise ValueError('No se pueden asignar puntos negativos')
	except ValueError:
		raise Exception('Ingrese numeros')
	return n1, n2


class Pelea:
	
	def __init__(self, retador, defensor):
		self.retador = [retador, 0]
		self.defensor = [defensor, 0]

	def cargar_resultado(self, n1, n2):
		n1, n2 = valida_entrada(n1, n2)
		self.retador[1] += n1
		self.defensor[1] += n2

	def obtener_ganador(self):
		if self.retador[1] == self.defensor[1]:
			return 'TIE'
		if self.retador[1] > self.defensor[1]:
			return self.retador[0]
		return self.defensor[0]


class HistorialDePeleas:
	
	def __init__(self):
		self.competidores = {}

	def cargar_pelea(self, pelea):
		ganador = pelea.obtener_ganador()
		self.competidores[ganador] = self.competidores.get(ganador, 0)
		self.competidores[ganador] += 1
		
	def obtener_record(self):
		record = ''
		cantidad = 0
		for competidor in self.competidores:
			if cantidad < self.competidores[competidor]:
				record = competidor
				cantidad = self.competidores[competidor]
		return record


pelea1 = Pelea('Juancho', 'Pepo')
pelea2 = Pelea('Juancho', 'Pancho')

pelea1.cargar_resultado(-1, 1)
pelea2.cargar_resultado(1, 6)
historial = HistorialDePeleas()
historial.cargar_pelea(pelea1)
print(historial.obtener_record())