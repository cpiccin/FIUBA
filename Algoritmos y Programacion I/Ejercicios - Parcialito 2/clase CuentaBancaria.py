class Cuenta:

	def __init__(self, nombre):
		self.nombre = nombre
		self.saldo_total = 0 
		self.motivo = []

	def __str__(self):
		return f'Cuenta de {self.nombre}'

	def saldo(self):
		return self.saldo_total

	def acreditar(self, cantidad, motivo):
		self.saldo_total += cantidad 
		self.motivo.append(('acreditación', cantidad, motivo))

	def extraer(self, cantidad, motivo):
		if cantidad > self.saldo_total:
			raise ValueError('Fondos Insuficientes')
		self.saldo_total -= cantidad
		self.motivo.append(('extracción', cantidad, motivo))

	def transferir(self, cantidad, cuenta2):
		if cantidad > self.saldo_total:
			raise ValueError('Fondos Insuficientes')
		self.saldo_total -= cantidad
		cuenta2.saldo_total += cantidad
		self.motivo.append(('extracción', cantidad, str(cuenta2)))
		cuenta2.motivo.append(('acreditación', cantidad, str(self)))

	def movimientos(self):
		return self.motivo


a = Cuenta('Candela Piccin')
b = Cuenta('Pepita Gomez')
print(a)
a.acreditar(500, 'Ahorro')
a.saldo()
a.acreditar(1400, 'Trolas')
a.transferir(1250, b)
print(a.movimientos())
print(b.movimientos())
