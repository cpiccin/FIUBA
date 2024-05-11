def ord_columnas(lista, n):
	contador = 0
	for e in lista:
		print(e, end=' ')
		contador += 1
		if contador == n:
			print()

ord_columnas([1,2,3,4,5,6], 3)