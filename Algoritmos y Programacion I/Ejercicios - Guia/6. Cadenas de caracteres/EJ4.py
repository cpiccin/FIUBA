from EJ2 import cada_tres_digitos

def separacion_de_miles(cadena):
	cadena_inversa = cadena[::-1]
	cadena_final = cada_tres_digitos(cadena_inversa, '.')
	return cadena_final[::-1]


