# a) Recibe una cadena y devuvelve un dic con la cantidad de veces que aparece la palabra

def cantidad(cadena):
	dic = {}
	for p in cadena.split():
		if p in dic:
			dic[p] += 1
			continue
		dic[p] = 1
	return dic 


# b) Cuenta la cantidad de apariciones de cada caracter en una cadena y devuelve en un diccionario

def caracteres(cadena):
	dic = {}
	for c in cadena: # NO IGNORA ESPACIOS
		if c in dic:
			dic[c] += 1
			continue
		dic[c] = 1
	return dic 


# c) Recibe una cantidad de iteraiones de una tirada de 2 dados y devuelve la cant de vees que se observa cada valor de la suma de los dos dados
from random import randint

def dados(n):
	dic = {}
	for _ in range(n):
		dado_1 = randint(1, 6)
		dado_2 = randint(1, 6)
		if dado_1 in dic:
			dic[dado_1] += 1
		else:
			dic[dado_1] = 1
		if dado_2 in dic:
			dic[dado_2] += 1
		else:
			dic[dado_2] = 1
	return dic

