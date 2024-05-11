def cadena_mas_larga(texto):
	dicc = {}
	cadena = ''.join(texto.split()).lower()
	
	for letra in cadena:
		if letra in dicc:
			continue 
		palabra_mayor = ''
		
		for palabra in texto.split():
			if letra in palabra.lower() and len(palabra) > len(palabra_mayor):
				palabra_mayor = palabra
	
		dicc[letra] = palabra_mayor

	return dicc


print(cadena_mas_larga('Chau'))


