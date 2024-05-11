def cerdos(cadena):
	lista = cadena.split()
	cad_final = []
	for p in lista:
		cad_final.append(p[1:]+p[0]+'ay')
	return ' '.join(cad_final)


print(cerdos('hola mundo'))