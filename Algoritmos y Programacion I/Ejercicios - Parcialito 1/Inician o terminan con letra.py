def main():

	texto = ''
	aux = 0
	while True:
		texto = input('Ingrese un texto: ')
		for c in texto:
			if c.isdigit():
				aux = 1
		if aux == 1:
			aux = 0
			continue
		break #sale del ciclo si no hay numeros en el texto

	letra = input('Ingrese una letra: ')
	while letra.isalpha() != True or len(letra) != 1:
		letra = input('Ingrese una letra: ')
	
	contador = 0
	for p in texto.split():
		if p[0] == letra or p[len(p)-1] == letra:
			contador += 1

	return contador


print(main())