from EJ5 import par_o_impar

def numeros_pares():
	num1 = int(input('Ingrese un numero: '))
	num2 = int(input('Ingrese otro numero: '))
	for x in range(num1, num2 + 1):
		if par_o_impar(x) == 1:
			print(x)
