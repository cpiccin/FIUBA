# a) Dado un numero entero n, indica si es par o no.

def par_o_impar(n):
	if n%2 == 0:
		return True
	else:
		return False

# b) Indica si n es primo o no.

def es_primo(n): 
	for x in range(2, n):
		if n%x == 0:
			return False
	return True
