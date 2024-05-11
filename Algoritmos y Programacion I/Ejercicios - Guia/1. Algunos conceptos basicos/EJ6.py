# a) Dados dos numeros, imprimir la suma, resta, division y multiplicacion de ambos

def operaciones(n1, n2):
	print(f'{n1} + {n2} = ', n1+n2)
	print(f'{n1} - {n2} = ', n1-n2)
	print(f'{n1} / {n2} = ', n1/n2)
	print(f'{n1} * {n2} = ', n1*n2)



# b) Dado un numero natural n, imprimir su tabla de multiplicar

def tabla_de_multiplicar(n):
	for x in range (1, 11):
		print(f'{n} * {x} = ', n*x)

