def elimina_pares(lista):
	if len(lista) == 0:
		return []
	if lista[0]%2 == 0:
		lista.remove(lista[0])
	return elimina_pares(lista[1:])

l1 = [1,2,3,4,5,6]
print(elimina_pares(l1))