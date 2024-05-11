def reemplaza(cadena):
	primera_letra = cadena[0]
	lista_cadena = list(cadena)
	for e in lista_cadena:
		if e == primera_letra:
			lista_cadena.insert(lista_cadena.index(e), '*')
			lista_cadena.pop(lista_cadena.index(e))
	return ''.join(lista_cadena)


print(reemplaza('comer caracoles es sano, claramente'))