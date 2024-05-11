lista = {332:4, 2355:12, 1982:3, 5757:6}
import csv

def compras(lista, precios_csv):

	# Chupetin x 3: 9 (Precio unidad: 3)

	with open(precios_csv) as precios:
		next(precios)

		for codigo,nombre,precio,desc in csv.reader(precios):
			codigo = int(codigo)
			precio = float(precio)
			if codigo in lista:
				print(f'{nombre} x {lista[codigo]}: {lista[codigo]*precio} (Precio unidad: {precio})')
			else:
				continue


compras(lista, 'precios.csv')
