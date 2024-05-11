def grep(nombre_archivo, cadena):
    '''Dada una cadena y un archivo imprime las lineas del archivo que contienen la cadena recibida'''
    with open(nombre_archivo, 'r') as nombre_archivo:
        for linea in nombre_archivo:
            if cadena in linea:
                print(linea.rstrip())


grep('poema.txt', '-Vamos')