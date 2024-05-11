# Algoritmo de Euclides

def euclides(m, n):
	while True: 
		resto = m % n
		if resto == 0: # se repite el ciclo hasta que el resto es 0
			return n
		m = n 
		n = resto


print(euclides(3, 6))