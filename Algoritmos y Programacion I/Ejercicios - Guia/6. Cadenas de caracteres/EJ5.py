# Dada una cadena de caracteres devuelve:

# a) La primera letra de cada palabra

def primeras_letras(cadena):
	lista = cadena.split()
	letras = ''
	for p in lista:
		letras += i[0]
	return letras

# b) La cadena con la primera letrade cada palabra en mayusculas

def primeras_letras_mayus(cadena):
	lista = cadena.split()
	lista_cadena = []
	for p in lista:
		lista_cadena.append(p.capitalize())
	return ' '.join(lista_cadena)

# c) Las palabras que comiencen con la letra 'A'

def letras_a(cadena):
	lista = cadena.split(' ')
	lista_cadena = []
	for p in lista:
		if p[0] in ('A', 'a', 'Á', 'á'):
			lista_cadena.append(p)
	return ' '.join(lista_cadena)

