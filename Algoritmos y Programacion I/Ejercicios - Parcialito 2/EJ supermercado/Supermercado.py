def supermercado(pedidos, archivo_salida):

	stock = {}
	with open(archivo_salida, 'w') as salida:

		for pedido in pedidos:
			for producto in pedido:

				if producto in stock:
					stock[producto] += pedido[producto]
					continue
				stock[producto] = stock.get(producto, pedido[producto])

		for producto, cant_total in stock.items():
			salida.write(f'{producto};{cant_total}\n')


pedidos = [{'arroz':3, 'quinoa':1, 'tomate':7},
		   {'ricota':4, 'durazno':5, 'coca cola':12, 'quinoa':2},
		   {'coca cola':8, 'manteca': 14, 'tomate':4}]


supermercado(pedidos, 'stock.txt')

				

