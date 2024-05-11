def elem_comunes(s1, s2):
	lista_final = []
	for e in s1:
		if e not in lista_final and e in s2:
			lista_final.append(e)
	return lista_final


print(elem_comunes([7,9,7,1],[6,9,7]))