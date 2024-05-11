import csv

def ganadores(lista_ganadora, ruta, premios):
	with open(ruta) as jugadores, open(premios, 'w') as salida:
		
		for linea in jugadores:
			linea = linea.rstrip('\n').split(',')
			jugador_x = linea[0]
			numeros = linea[1].split('-')
			contador = 0
			for numero in numeros:
				numero = int(numero)
				if numero in lista_ganadora:
					contador += 1
			if contador >= 2:
				salida.write(f'{jugador_x},{contador}\n')
			contador = 0




lista = [10, 15, 4, 156, 69]

ganadores(lista, 'Participantes.csv', 'premios.csv')