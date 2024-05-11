def edad(archivo_edades):
	edad_mas_alta = 0
	misma_edad = []
	with open(archivo_edades) as edades:
		for linea in edades:
			linea = linea.rstrip('\n').split(',')
			linea[1] = int(linea[1])

			if linea[1] == edad_mas_alta:
				misma_edad.append(linea[0])
			
			if linea[1]>edad_mas_alta:
				misma_edad = []
				misma_edad.append(linea[0])
				edad_mas_alta = linea[1]
	
	return edad_mas_alta, misma_edad
			
print(edad('Edades.txt'))