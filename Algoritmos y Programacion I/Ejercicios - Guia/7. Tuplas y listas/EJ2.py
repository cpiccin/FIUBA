# a) Indica si dos fichas de domino encajan. Son recibidas en tuplas

def encaja_domino_tupla(ficha1, ficha2):
	if ficha1[1] == ficha2[0]:
		return True
	return False


# b) Indica si dos fichas de domino encajan o no. Las fichas son recibidas en cadenas

def encaja_domino_cadena(ficha1, ficha2):
	ficha1 = ficha1.split('-')
	ficha2 = ficha2.split('-')
	if ficha1[1] == ficha2[0]:
		return True
	return False

