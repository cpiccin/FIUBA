from Cola import Cola
from Pila import Pila

def invertir_primeros_k(cola, k):
	pila = Pila()
	resto = Cola()
	while not cola.esta_vacia():
		for _ in range(k):
			try:
				pila.apilar(cola.desencolar())
				# print('COLA: ',cola)
				# print('PILA: ',pila)
			except ValueError:
				break
		while True:
			if cola.esta_vacia():
				break
			resto.encolar(cola.desencolar())
			# print('RESTO: ', resto)
		break
	while not pila.esta_vacia():
		cola.encolar(pila.desapilar())
	while not resto.esta_vacia():
		cola.encolar(resto.desencolar())


c1 = Cola()
c1.encolar(1)
c1.encolar(2)
c1.encolar(3)
c1.encolar(4)
c1.encolar(5)
# print('sin invertir: ', c1)
invertir_primeros_k(c1, 7)
print(c1)