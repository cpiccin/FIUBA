# Dada una cadena de caracteres

# a) Devuelve solo las consonantes

def solo_consonantes(cadena):
	cadena_final = '' 
	for c in cadena:
		if c in 'aeiouAEIOU':
			continue
		cadena_final += c 
	return cadena_final

# b) Devuelve solo las vocales

def solo_vocales(cadena):
	cadena_final = ''
	for c in cadena:
		if c in ' aeiouAEIOU':
			cadena_final += c
	return cadena_final

# c) Reemplaza cada vocal por su siguiente vocal

def sig_vocal(cadena):
	lista_cadena = []
	vocales = ['a', 'e', 'i', 'o', 'u']
	for c in cadena:
		if c in vocales:
			lista_cadena.append(vocales[vocales.index(c) - 4])
		else:
			lista_cadena.append(c)	
	return ''.join(lista_cadena)


# d) Indica si se trata de un palindromo

def es_palindromo(cadena):
	cadena_unida = ''.join(cadena.split(' '))
	cadena_unida_inversa = cadena_unida[::-1]
	if cadena_unida == cadena_unida_inversa:
		return True
	return False


