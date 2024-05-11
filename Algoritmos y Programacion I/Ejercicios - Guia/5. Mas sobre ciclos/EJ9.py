#  reciba dos números como parámetros, y devuelva cuántos múltiplos del primero hay, que sean menores que el segundo.

# a) Utilizando un ciclo for desde el primer numero hasta el segundo

def multiplos_inferiores_for(n1, n2):
	cantidad = 0
	for i in range(1, n2):
		if n1*i < n2:
			cantidad += 1
	return cantidad


# b) Utilizando un ciclo while que multiplique el primer numero hasta que sea mayor que el segundo

def multiplos_inferiores_while(n1, n2):
	i = 1
	cantidad = 0
	while n1*i < n2:
		i += 1
		cantidad += 1
	return cantidad

# La implementacion con while me parece mas clara ademas de que es la que menos 
# operaciones realiza porque for itera por cada numero entre 1 y n2 pero while
# deja de iterar antes cuando se cumple la condicion 






