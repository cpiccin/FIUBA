import csv

def intercambia_columnas(ruta_entrada, ruta_salida, c1, c2):
	with open(ruta_entrada) as entrada, open(ruta_salida, 'w') as salida:
		writer = csv.writer(salida)
		for fila in csv.reader(entrada):
			if c1 > len(fila) or c2 >= len(fila):
				raise IndexError('La columna esta fuera de rango')
			fila[c1], fila[c2] = fila[c2], fila[c1]
			writer.writerow(fila)

def main():
	try:
		c1 = int(input('Ingrese columna 1: ')) - 1
		c2 = int(input("Ingrese columna 2: ")) - 1
	except ValueError:
		print('Ingresa numeros no cadenas')
		return

	try: 
		intercambia_columnas('entrada.csv', 'salida.csv', c1, c2)
	except IOError:
		print('No se pudo abrir el archivo')
	except IndexError:
		print('El archivo de entrada no tiene la columna pedida')
