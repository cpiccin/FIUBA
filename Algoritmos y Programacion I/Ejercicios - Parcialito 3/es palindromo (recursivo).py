# Escribir una funcion recursiva que reciba una cadena y devuelva True si es un palındromo
# (se lee igual hacia adelante que hacia atras) o False si no lo es.

def es_palindromo(cadena):
	cadena_unida = ''.join(cadena.split(' '))
	cadena_unida_inversa = cadena_unida[::-1]
	if cadena_unida == cadena_unida_inversa:
		return True
	return False


def es_palindromo_recursivo(cadena):
    cadena = ''.join(cadena.split(' '))
    if len(cadena) == 0 or len(cadena) == 1:
        return True
    if cadena[0] != cadena[len(cadena)-1]:
        return False
    return es_palindromo_recursivo(cadena[1:-1])
    
cadena = 'rotor'
cadena1 = 'ornamenro'
cadena2 = 'anita lava la tina'
print(es_palindromo_recursivo(cadena))
print(es_palindromo_recursivo(cadena1))
print(es_palindromo_recursivo(cadena2))