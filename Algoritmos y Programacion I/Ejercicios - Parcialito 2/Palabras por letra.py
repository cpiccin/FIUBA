def equis(cadena):
	res = {}
	for palabra in cadena.split():
		if palabra[0].lower() in res:
			res[palabra[0].lower()].append(palabra)
			continue
		res[palabra[0].lower()] = res.get(palabra[0].lower(), [palabra])
	return res


print(equis('Este es el parcial de algoritmos'))