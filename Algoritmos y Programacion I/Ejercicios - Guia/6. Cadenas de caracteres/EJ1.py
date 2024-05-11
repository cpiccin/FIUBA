# Funciones que dada una cadena de caracteres:

# a) Imprime los dos primeros caracteres

def dos_primeros_caracteres(cadena):
	print(cadena[0:2])

# b) Imprime los tres ultimos caracteres

def tres_ultimos_caracteres(cadena):
	print(cadena[-3:])

# c) Imprime la cadena cada dos caracteres

def cada_dos_caracteres(cadena):
	print(cadena[::2])

# d) Imprime la cadena en sentido inverso

def sentido_inverso(cadena):
	print(cadena[::-1])

# e) Imprime la cadena en un sentido y en sentido inverso

def imprime_reflejo(cadena):
	print(cadena + cadena[::-1])
