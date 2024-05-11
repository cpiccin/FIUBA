def elimina_sucesivos_primos(L):
	return _elimina_sucesivos_primos(L, [])

def _elimina_sucesivos_primos(lista, nueva):
	if len(lista) == 1:
		nueva.append(lista[0])
		return nueva
	if not es_primo(lista[1]):
		nueva.append(lista[0])
	return _elimina_sucesivos_primos(lista[1:], nueva)

def es_primo(n): 
	for x in range(2, n):
		if n%x == 0:
			return False
	return True


l1 = [1,2,3,4,5,6,7,8]

print(elimina_sucesivos_primos(l1))
