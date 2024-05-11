def invertido(cadena):
	lista_cadena = cadena.split()
	lista_final =[]
	for e in lista_cadena:
		lista_final.append(e[::-1])
	return ' '.join(lista_final)


print(invertido('Que dia tan bonito'))