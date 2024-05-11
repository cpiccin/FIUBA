# Dada una cadena y un caracter

# a) Inserta el caracter entre cada letra de la cadena

def caracter_separador(cadena, c):
	print(cadena.replace('', c)[1: -1])

# b) Reemplaza todos los espacios por el caracter

def reemplaza_espacios(cadena, c):
	print(cadena.replace(' ', c))

# c) Reemplaza todos los digitos en la cadena por el caracter

def reemplaza_digitos(cadena, c):
    cadena_final = ''
    for x in cadena:
        if x.isdigit() == True:
            cadena_final += c
        else:
            cadena_final += x
    return cadena_final

# d) Inserta el caracter cada 3 digitos de la cadena

def cada_tres_digitos(cadena, c):
	cadena_final = ''
	contador = 0
	for x in cadena:
		cadena_final += x
		contador += 1
		if contador%3 == 0:
			cadena_final += c
	return cadena_final


