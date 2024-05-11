# a) Dada una lista, devuelve una nueva lista igual a la original pero invertida

def lista_invertida(lista):
	for i in range(len(lista)):
		lista.insert(i,lista.pop())
	return lista

