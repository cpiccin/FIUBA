from string import ascii_lowercase

def pangrama(cadena):
	contador = 0
	lista_letras = []
	for e in list(cadena):
		if e not in lista_letras:
			if e in ascii_lowercase:
				contador += 1
				lista_letras.append(e)
	if len(lista_letras) == len(ascii_lowercase):
		return True
	return False


print(pangrama('mr. jock, tv quiz phd., bags few lynx'))