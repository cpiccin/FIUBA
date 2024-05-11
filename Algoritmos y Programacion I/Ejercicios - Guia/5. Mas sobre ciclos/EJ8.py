def cantidad_suma_promedio():
	cantidad = 0
	suma_total = 0
	promedio = 0
	while True:
		numero = int(input('Ingrese un numero (-1 para terminar): '))
		if numero == -1:
			print('Cantidad de numeros ingresados: ', cantidad)
			print('Suma total de los valores: ', suma_total)
			print('Promedio de los valores: ', suma_total/cantidad)
			break
		cantidad += 1
		suma_total += numero
		
		continue


cantidad_suma_promedio()