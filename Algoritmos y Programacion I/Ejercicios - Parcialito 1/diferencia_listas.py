def diferencia_listas(l1, l2):
	'''devuelve todos los elementos de l1 que no estan en l2'''
	lista_final = []
	for e in l1:
		if e not in l2:
			lista_final.append(e)
	return lista_final

print(diferencia_listas([15,49],[6,31]))