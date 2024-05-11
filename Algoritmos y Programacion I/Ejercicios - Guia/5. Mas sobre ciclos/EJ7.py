# a) Una funcion que devuelve la suma de todos los divisores de un numero n, sin incluirlo

def suma_divisores(n):
	suma = 0 
	for x in range(1, n):
		if n%x == 0:
			suma += x
	return suma


# b) Imprime los primeros m numeros tales que la suma de sus divisores sea igual a si mismo

def numeros_perfectos(m):
	for x in range(1, m+1):
		if suma_divisores(x) == x:
			print(x)
		continue


# c) Imprime las primeras m parejas de numeros (a, b) que sean parejas de numeros amigos

def numeros_amigos(m):
	for i in range(1, m+1):
		for j in range(i, m+1):
			if i==j or j==i:
				continue
			if suma_divisores(i) == j and suma_divisores(j) == i:
				print((i, j))



 




