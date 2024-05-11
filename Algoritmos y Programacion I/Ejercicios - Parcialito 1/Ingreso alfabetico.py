def main():
	cadena_final = []
	while True:
		entrada = input('ingrese una letra: ')
		if len(entrada) == 0:
			break
		if len(entrada) == 1 and entrada.isalpha():
			cadena_final.append(entrada)
	return ''.join(sorted(cadena_final))

print(main())