from math import log  #log(x,base)

# a) 

def es_potencia_de_dos(n):
	if n<1:
		return False
	if round(log(n, 2)) == log(n, 2): # si al redondearlo es igual a sin redondear significa q es un num entero
		return True
	return False

# b) 

def potencias_de_dos(n1, n2):
	total = 0
	for x in range(n1, n2+1):
		if es_potencia_de_dos(x) == True:
			total += x
	return total


print(potencias_de_dos(2, 7))


