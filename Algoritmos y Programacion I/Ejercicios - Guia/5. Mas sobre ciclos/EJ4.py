from random import randrange

def numero_secreto():
	numero_secreto = randrange(1, 25)
	entrada = int(input('Ingresa un numero incial: '))
	while entrada != numero_secreto:
		if entrada < numero_secreto:
			entrada = int(input('El numero secreto es mayor. Elegi otro: ')) 
		if entrada > numero_secreto:
			entrada = int(input('El numero secreto es menor. Elegi otro: '))
	print(f'Encontraste el numero {numero_secreto}!')

numero_secreto()