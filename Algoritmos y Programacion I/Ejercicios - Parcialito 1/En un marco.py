def main():
	entrada = ' '
	lista_palabras = []
	secuencia_mayor = 0
	while len(entrada)!=0:
		entrada = input('Ingrese una linea o enter para terminar: ')
		lista_palabras.append(entrada)
	for i in range(len(lista_palabras)):
		if len(lista_palabras[i])>secuencia_mayor:
			secuencia_mayor = len(lista_palabras[i])
			continue
	print('*'*(secuencia_mayor+2))
	for i in lista_palabras:
		if len(i)==0:
			continue
		print('*',i,' '*(secuencia_mayor-len(i)),'*', sep='')
	print('*'*(secuencia_mayor+2))


main()


