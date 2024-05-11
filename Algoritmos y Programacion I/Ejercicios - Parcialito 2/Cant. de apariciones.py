def cant_de_apariciones(cadena):
	res = {}

	for letra in cadena.lower():

		if letra in res:
			res[letra] += 1 
			continue
		res[letra] = res.get(letra, 1)

	return res


print(cant_de_apariciones('Catamarca'))