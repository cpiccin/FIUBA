def promedio():
	total = 0
	cantidad = 0
	while True:
		nota = float(input('Ingrese una nota: '))
		total += nota
		cantidad += 1
		print(total/cantidad)
		seguir = input('Desea ingresar mas notas? (si/no) ')
		if seguir == 'si':
			continue
		return print('Promedio final: ', total/cantidad)

promedio()