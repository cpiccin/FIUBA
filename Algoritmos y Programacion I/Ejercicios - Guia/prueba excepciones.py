def division():

	while True:
		try:
			n1 = int(input('Ingrese un numero inicial: '))
			n2 = int(input('Ingrese un numero final: '))
			break
		except ValueError:
			print('No se pueden dividir palabras')

	try:
		print(n1/n2)
	except ZeroDivisionError:
		print('No se puede dividir por 0 salamin')

	print('Programa terminado')



def division2():

	try:
		n1 = int(input('Ingrese un numero inicial: '))
		n2 = int(input('Ingrese un numero final: '))
		print(n1/n2) 

	except ValueError:
		print('Valor erroneo')

	except ZeroDivisionError:
		print('No se puede dividir entre 0')

	finally:
		print('Programa finalizado')



def pedir_entero():
	intentos = 0
	while intentos < 5:
		valor = input('Ingrese un entero: ')
		try:
			return int(valor)
		except ValueError:
			print(f'{valor} no es un entero.')
			intentos += 1
	raise ValueError('No ingresaste nada bien en 5 intentos.')


pedir_entero()
