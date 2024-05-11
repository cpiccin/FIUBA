# a) Le pregunta al usuario la contrasenia ya almacenada y no le deja continuar hasta que sea la correcta

def contraseña_almacenada():
	contraseña = 'holaDonJose123'
	ingreso = ''
	while ingreso != contraseña:
		ingreso = input('Ingrese contraseña: ')
	print('Bienvenido!')

# b) Ahora solo se permite una cantidad limitada de intentos

def contraseña_con_intentos():
	contraseña = 'holaDonJose123'
	intentos = 0
	while intentos < 3:
		ingreso = input('Ingrese contraseña: ')
		if ingreso == contraseña:
			return print('Bienvenido!')
		intentos += 1
		print(f'Le quedan {3 - intentos} intentos')
	print('Intentos agotados')

# c) Ahora despues de cada intento hay una pausa cada vez mayor

from time import sleep

def contraseña_con_pausa():
	contraseña = 'holaDonJose123'
	intentos = 0
	espera = 0
	while intentos < 3:
		ingreso = input('Ingrese contraseña: ')
		intentos += 1
		if ingreso == contraseña:
			return print('Bienvenido!')
		espera += 1
		print(f'Le quedan {3 - intentos} intentos. Espere {espera} segundos para volver a intentar')
		sleep(espera)
	print('Intentos agotados.')

# d) Ahora, el programa anterior es una funcion que devuelve devuelve si el usuario ingreso o no la contra correctamente con un True o False

def contraseña_correcta(ingreso, contraseña):
	if ingreso == contraseña:
		return True
	return False


