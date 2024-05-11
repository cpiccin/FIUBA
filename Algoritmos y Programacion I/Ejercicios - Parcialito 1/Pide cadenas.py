def pide_cadenas():
	cadena = ''
	while True:
		entrada = input('Cadena: ')
		if entrada == '':
			break
		cadena += entrada
	return cadena.split()


print(pide_cadenas())
