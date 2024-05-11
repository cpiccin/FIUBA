def gim_mas_cercano(archivo_entrada, archivo_salida, gimnasios):

	with open(archivo_entrada) as entrada, open(archivo_salida, 'w') as salida:
		
		for linea in entrada:
			
			linea = linea.rstrip('\n')

			pokemon, tipo, pos = linea.split(';')
			pos_x, pos_y = pos.split(',')
			pos_x, pos_y = int(pos_x), int(pos_y)

			nombre_gim = obtener_mas_cercano(gimnasios, pos_y, pos_x)

			salida.write(f'{pokemon};{tipo};{nombre_gim}')

from math import inf

def obtener_mas_cercano(gimnasios, pos_y, pos_x):
	gim_cercano = None
	menor_dist = inf 
		
	for gim in gimnasios:

		gim_x, gim_y = gimnasios[gim]
		dist_actual = abs(pos_x-gim_x) + abs(pos_y-gim_y)

		if menor_dist > dist_actual:
			menor_dist = dist_actual
			gim_cercano = gim 

	return gim_cercano

gimnasios = {
    'Pewter City Gym': (20, 30),
    'Cerulean Gym': (15, 20),
    'Vermilion Gym': (-10, -10),
    'Celadon Gym': (40, 40),
    'Fuchsia City Gym': (25, 10)
}

import csv

def gim_mas_cercano_csv(archivo_entrada, archivo_salida, gimnasios):

	with open(archivo_entrada) as entrada, open(archivo_salida, 'w') as salida:

		writer = csv.writer(salida, delimiter=';')

		for pokemon, tipo, pos in csv.reader(entrada, delimiter=';'):

			pos_x, pos_y = pos.split(',')
			pos_x, pos_y = int(pos_x), int(pos_y)

			nombre_gim = obtener_mas_cercano(gimnasios, pos_y, pos_x)

			writer.writerow([pokemon, tipo, nombre_gim])


