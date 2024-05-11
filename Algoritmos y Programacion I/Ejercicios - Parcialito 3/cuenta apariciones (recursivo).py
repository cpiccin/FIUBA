# Escribir una funcion recursiva en Python que cuente la cantidad
# de apariciones de un elemento en una lista recibidos por parametro.

def cantidad_de_apariciones(lista, e):
	suma = 0
	if len(lista) == 0:
		return 0 
	if lista[0] == e:
		suma = 1
	return cantidad_de_apariciones(lista[1:], e) + suma

lista = [4,4,4,4,4,4,4,4]

print(cantidad_de_apariciones(lista, 4))