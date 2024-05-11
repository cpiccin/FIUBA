def censura(texto, palabra):
	n = len(palabra)
	lista_texto = texto.split()
	cadena_final = []
	cadenas = (palabra.capitalize(), palabra.upper(), palabra.lower())
	for e in lista_texto:
		if e in cadenas:
			cadena_final.append('*'*n)
		else:
			cadena_final.append(e)
	return ' '.join(cadena_final)



print(censura('Un tete a tete con Tete', 'tete'))
