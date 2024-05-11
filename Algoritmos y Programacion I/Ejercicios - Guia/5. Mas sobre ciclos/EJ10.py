def es_primo(n):
	for x in range(2, n):
		if n%x == 0:
			return False
	return True


def numeros_primos(n):
	for x in range(n):
		if es_primo(x) == True:
			print(x)
		continue
