def frecuencia(texto):
	res = {}
	for palabra in texto.split():
		if palabra in res:
			res[palabra] += 1
			continue
		res[palabra] = res.get(palabra, 1)
	return res


def maxima_frecuencia(frecuencia):
	lista = []
	maxima_frecuencia = 0
	for palabra in frecuencia:
		if frecuencia[palabra] > maxima_frecuencia:
			lista = []
			lista.append(palabra)
			maxima_frecuencia = frecuencia[palabra]
			continue
		if frecuencia[palabra] == maxima_frecuencia:
			lista.append(palabra)
	return lista


texto = 'habia habia a a a a a una vez truz cuantas veces te dije que no me importa tu carisma ni tu pelo ni tu amor yo quiero un avestruz habia un'

diccionario = frecuencia(texto)

print(maxima_frecuencia(diccionario))
