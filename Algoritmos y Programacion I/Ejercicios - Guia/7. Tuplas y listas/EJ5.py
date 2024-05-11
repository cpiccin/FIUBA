# Dada una lista de numeros enteros:

# Funciones auxiliares de ej anteriores
def es_primo(n):
	if n == 1:
		return False 
	for x in range(2, n):
		if n%x == 0:
			return False
	return True

def factorial(n):
	factorial = 1
	for x in range(1, n+1):
		factorial *= x
	return factorial

# a) Devuelve una lista con todos los que sean primos
def lista_primos(lista):
	lista_final = []
	for n in lista:
		if es_primo(n) == True:
			lista_final.append(n)
	return lista_final


# b) Devuelve la sumatoria y el promedio de los valores

def sumatoria_promedio(lista):
	sumatoria = 0
	cantidad = 0
	for n in lista:
		sumatoria += lista[enteros.index(n)]
		cantidad += 1
	return (sumatoria, sumatoria/cantidad)


# c) Devuelve una lista con el factorial de cada numero

def lista_factoriales(lista):
	lista_final = []
	for n in lista:
		lista_final.append(factorial(lista[n]))
	return lista_final