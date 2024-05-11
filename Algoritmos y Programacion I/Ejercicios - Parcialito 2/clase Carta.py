class Carta:

	def __init__(self, palo, valor):
		self.palo = palo
		self.valor = valor 

	def __str__(self):
		return f'{self.valor} de {self.palo}'

	def compara_cartas(self, carta2):
		if self.palo == carta2.palo:
			if self.valor < carta2.valor:
				return f'La carta {str(self)} es menor a {str(carta2)}'
			if self.valor > carta2.valor:
				return f'La carta {str(self)} es mayor a {str(carta2)}'
			if self.valor == carta2.valor:
				return 'Ambas cartas son iguales!'
		if self.palo != carta2.palo:
			if self.palo < carta2.palo:
				return f'{str(self)} es menor que {str(carta2)}'
			if self.palo > carta2.palo:
				return f'{str(self)} es mayor que {str(carta2)}'