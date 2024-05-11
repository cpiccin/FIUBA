def pedir_entero(mensaje, min, max):
    entrada = (input(f'{mensaje} [{min}..{max}]: '))
    while '-' in entrada and (entrada[1:].isdigit() == False):
        print(f'Por favor ingresa un número entre {min} y {max}.')
        entrada = (input(f'{mensaje} [{min}..{max}]: '))
    while int(entrada) < min or int(entrada) > max:
        print(f'Por favor ingresa un número entre {min} y {max}.')
        entrada = (input(f'{mensaje} [{min}..{max}]: '))
    return entrada


z = pedir_entero('Decime tu numero favorito', -5, 10)

print(z)