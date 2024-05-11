import csv

def autores(archivo_entrada):
	res = {}
	with open(archivo_entrada) as entrada:
		for linea in csv.reader(entrada):
			autores = linea[2].split('-')
			for autor in autores:
				if autor in res:
					res[autor].append(linea[1])
					continue
				res[autor] = res.get(autor, [linea[1]])
	return res 


print(autores('autores.csv'))
