from string import ascii_lowercase

def valida(intentos):
	letras = (ascii_lowercase, ascii_lowercase.upper())
	c_especiales = ('!@~#$')
	cant_letras = 0
	cant_num = 0
	cant_c_esp = 0
	cant_intentos = 0
	while cant_intentos < intentos:
		entrada = input('ingrese una contra: ')
		for c in entrada:
			if c.isdigit():
				cant_num += 1
			if c.isalpha():
				cant_letras += 1
			if c in c_especiales:
				cant_c_esp += 1
		if not (2<=cant_num<cant_letras and 1<=cant_c_esp<=3):
			cant_letras, cant_num, cant_c_esp = 0, 0, 0
			cant_intentos += 1
			continue
		return (intentos - cant_intentos-1)
	print('intentos agotados')
	return (-1)

print(valida(3))


