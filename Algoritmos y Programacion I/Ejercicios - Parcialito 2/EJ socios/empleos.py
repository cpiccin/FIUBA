import csv

def imprime(archivo_socios):
	# no graduados, con empleo, menores de 35
	with open(archivo_socios) as socios:
		next(socios)
		for linea in csv.reader(socios):
			if int(linea[4]) == 1 and int(linea[5]) == 0 and 0<int(linea[2])<35:
				print(', '.join(linea[:4]), ', Tiene empleo, Termino el secundario')


imprime('socios.csv')