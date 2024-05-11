def transforma(cadena, transformaciones):

	res = ''

	for letra in cadena:
		if letra in transformaciones:
			res += transformaciones[letra]
			continue
		res += letra

	return res


dic = {'H': 'e', 'o': 'b', 'l':'m'}
print(transforma('Hola', dic))