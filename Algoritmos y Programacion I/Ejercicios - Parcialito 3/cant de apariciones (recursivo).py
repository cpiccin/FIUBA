# Escribir una función recursiva que recibe una cadena s
# y un caracter c, y devuelve la cantidad de apariciones
# de c en s. 


def apariciones(s, c):
	if len(s) == 0:
		return 0
	suma = 0
	if s[0] == c:
		suma = 1
	return apariciones(s[1:], c) + suma

print(apariciones('', 'a'))