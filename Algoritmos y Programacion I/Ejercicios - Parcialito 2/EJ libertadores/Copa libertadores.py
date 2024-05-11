import csv

def copas(archivo_entrada, archivo_salida):

	with open(archivo_entrada) as entrada, open(archivo_salida, 'w') as salida:
		next(entrada)
		dicc = {}

		for año,campeon in csv.reader(entrada):
			if campeon in dicc:
				dicc[campeon] += 1 
				continue
			dicc[campeon] = dicc.get(campeon, 1)
		for campeon in dicc:
			salida.write(f'{campeon} {dicc[campeon]}\n')


copas('Ganadores libertadores.csv', 'Cantidad de copas.csv')

