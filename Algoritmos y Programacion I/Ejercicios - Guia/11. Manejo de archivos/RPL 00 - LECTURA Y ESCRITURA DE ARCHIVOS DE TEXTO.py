def leer_primera_linea(nombre_archivo):
    '''Devuelve la primer linea del archivo sin el salto de linea si lo tiene'''
    with open(nombre_archivo, 'r') as nombre_archivo:
        return nombre_archivo.readline().rstrip('\n')

def escribir_en_archivo(contenido, nombre_archivo):
    '''Escribe el valor de contenido al archivo nombre_archivo, reemplazando su contenido existente'''
    with open(nombre_archivo, 'w') as nombre_archivo:
        nombre_archivo.write(contenido)



escribir_en_archivo('CHAU', 'llegada.txt')
linea = leer_primera_linea('llegada.txt')
print(linea)