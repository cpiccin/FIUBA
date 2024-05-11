# Realizar una función recursiva en Python que reciba un número
# entero y devuelva el producto de sus dígitos. 
# Ejemplo: producto_digital(356) → 90

def producto_digital(n):
	n = str(n)
	if len(n) == 1:
		return int(n) 
	return producto_digital(n[1:])*int(n[0])


def producto_digital_sin_str(n):
	if n%10 == n:
		return n 
	return producto_digital_sin_str(n//10)*(n%10)

print(producto_digital_sin_str(356))
print(producto_digital_sin_str(123))
