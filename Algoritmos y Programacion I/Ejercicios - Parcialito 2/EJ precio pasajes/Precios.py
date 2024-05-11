import csv

def precio_mas_barato(ruta):
	res = {}

	with open(ruta) as pasajes:

		for fecha, destino, precio in csv.reader(pasajes):

			if destino in res:
				if res[destino][1] > precio:
					res[destino] = (fecha, precio)
				continue
			res[destino] = res.get(destino, (fecha, precio))

	return res 


print(precio_mas_barato('pasajes.txt'))