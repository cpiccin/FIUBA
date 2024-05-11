def valida(minuto, segundo):
	if 0<=minuto<=59 and 0<=segundo<=59:
		return minuto, segundo
	raise ValueError('El angulo es invalido')

class Angulo:
	def __init__(self, grado, minuto, segundo):
		self.grado = grado
		self.minuto, self.segundo = valida(minuto, segundo)

	def __str__(self):
		return f"{self.grado}° {self.minuto}' {self.segundo}''"

	def sumar_segundos(self, segundos):
		seg = self.segundo + segundos 
		minuto = self.minuto 
		grado = self.grado
		if seg > 60:
			minuto += seg/60
			seg = seg - 60*mi

