def reordena(lista):
	lista_pares = []
	lista_impares = []
	for n in lista:
		if n%2 == 0:
			lista_pares.append(n)
		else:
			lista_impares.append(n)
	for e in lista_impares:
		lista_pares.append(e)
	return lista_pares


print(reordena([3,5,2,6,18,7,40,11]))
