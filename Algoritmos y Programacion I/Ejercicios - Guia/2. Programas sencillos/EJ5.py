# a) Dado un numero entero devuelve 0 si es impar y 1 si es par

def par_o_impar(n):
	if n%2 == 0:
		return 1
	return 0


# b) Dado un numero entero devuelve 0 si es impar y 1 si es par

def par_o_impar_opuesto(n):
	if n%2 == 0:
		return 0
	return 1


# c) Dado un numero entero devuelve el digito de las unidades. Ej. para 153 debe devolver 3

def digitos_de_unidades(n):
	contador = 0
	for x in str(n):
		contador += 1
	return contador


# d) Dado un número devuelve el primer número múltiplo de 10 inferior a él. Ej.para 153 debe devolver 150

def multiplos_inferiores(n):
	for x in range(0, n + 1, 10):
		if (n-10) < x:
			return x

