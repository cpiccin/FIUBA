def capitalizacion(cadena):
	lista_cadena = cadena.split()
	lista_final = []
	for e in lista_cadena:
		lista_final.append(e.capitalize())
	return ' '.join(lista_final)


print(capitalizacion('hola, como estas'))