# Continuacion de la agenda.
# Escribir un programa que le vaya solicitando al usuario que ingrese nombres

# a) Si el nombre esta en la agenda, debe mostrar el telefono y, opcional, permitir modificarlo
# b) Si el nombre no esta, tiene que permitir ingresar el telefono correspondiente
# si usa '*' sale del programa

def agenda():
	nombre = ''
	tel = ''
	agenda = {}
	while True:
		nombre = input('Ingrese un nombre: ')
		if nombre == '*':
			break
		if nombre in agenda:
			print(agenda[nombre], '. Es correcto este numero?')
			tel = input('S/N: ')
			if tel == 'N':
				agenda[nombre] = int(input('Ingrese nuevo numero: '))
			continue
		agenda[nombre] = int(input('Ingrese un numero de telefono: '))
	return agenda


print(agenda())
