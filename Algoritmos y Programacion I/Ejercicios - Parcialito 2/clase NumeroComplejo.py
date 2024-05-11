def num_valido(real, imaginario):
	if type(real) != int or type(imaginario) != int:
		raise ValueError('No son numeros')
	return real, imaginario


class NumeroComplejo:

	def __init__(self, real, imaginario):
		self.real, self.imaginario = num_valido(real, imaginario)


	def __str__(self):
		return f'{self.real} + {self.imaginario}i'


	def __add__(self, n2):
		return NumeroComplejo(self.real + n2.real, self.imaginario + n2.imaginario)


	def __mul__(self, n2):
		return NumeroComplejo(self.real*n2.real-self.imaginario*n2.imaginario, self.real*n2.imaginario+self.imaginario*n2.real)



n1 = NumeroComplejo(2, 3)
n2 = NumeroComplejo(4,1)
print(n1, ' y ', n2)
print(n1*n2)