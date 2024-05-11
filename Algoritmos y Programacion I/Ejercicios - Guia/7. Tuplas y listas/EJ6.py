# Dada una lista de numeros enteros y un entero k:

NUMEROS = [0, 15, 3, 4, 5, 75, 7, 8, 4735]
k = 5

# a) Devuelve tres listas, una con los menores, otra con los mayores y otra con los iguales a k

def listas_de_k(numeros, k):
	menores = []
	mayores = []
	iguales = []
	for n in numeros:
		if n < k:
			menores.append(n)
		if n > k:
			mayores.append(n)
		if n == k:
			iguales.append(n)
	return menores, mayores, iguales


# b) Devuelve una lista con aquellos que son multiplos de k

def multiplos_de_k(numeros, k):
	multiplos = [0]
	for n in numeros:
		if n == 0:
			continue
		if n%k == 0:
			multiplos.append(n)
	return multiplos


