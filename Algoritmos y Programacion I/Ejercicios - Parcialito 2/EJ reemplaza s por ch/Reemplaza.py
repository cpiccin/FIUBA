def reemplaza(archivo_entrada, archivo_salida):

	with open(archivo_entrada) as entrada, open(archivo_salida, 'w') as salida:
		for linea in entrada:
			for char in linea:
				if char == 's':
					salida.write('ch')
					continue
				salida.write(char)


reemplaza('entrada.txt', 'salida.txt')