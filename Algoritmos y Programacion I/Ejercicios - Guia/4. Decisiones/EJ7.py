def en_numeros_romanos(año):
	lista_num = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
	lista_letras = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
	romano_final = ''
	i = 0
	while año > 0: 
		for x in range(año//lista_num[i]):
			romano_final += lista_letras[i]
			año -= lista_num[i]
		i += 1
	return romano_final


print(en_numeros_romanos(100))
print(en_numeros_romanos(1000))
print(en_numeros_romanos(1))
print(en_numeros_romanos(2343))
print(en_numeros_romanos(0))