def camelcase(cadena):
	lista_cadena = cadena.split('_')
	cadena_final = ''
	for e in lista_cadena:
		cadena_final += e.capitalize()
	return cadena_final


