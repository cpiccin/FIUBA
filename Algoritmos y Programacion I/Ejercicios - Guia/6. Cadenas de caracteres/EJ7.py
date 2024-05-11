# Dadas dos cadenas de caracteres

# a) Indica si la segunda cadena es subcadena de la primera

def verifica_subcadena(cadena, subcadena):
	if subcadena in cadena:
		return True
	return False


# b) Devuelve la que sea anterior en orden alfabetico

def alfabetico(cadena1, cadena2):
	lista = [cadena1, cadena2]
	lista.sort()
	return lista[0]

