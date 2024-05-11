''' Escribir una función, llamada cp, que copie todo el contenido de un archivo (sea
de texto o binario) a otro, de modo que quede exactamente igual.
Nota: utilizar archivo.read(bytes) para leer como máximo una cantidad de bytes.'''


def cp(file1, file2):
	with open(file1, 'rb') as file1, open(file2, 'wb') as file2:
		file2.write(file1.read(21))


cp('poema.txt', 'llegada.txt')