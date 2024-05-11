def binario(cadena):
	contador = 0
	en_decimal = 0
	for x in cadena[::-1]:
		if num == "1":
			en_decimal += 2**contador
		contador += 1
	print(en_decimal)

