def wc(nombre_archivo):
    '''Dado un archivo de texto, imprime cuantas lineas, palabras y caracteres contiene el archivo'''
    lineas = 0
    palabras = 0
    caracteres = 0
    with open(nombre_archivo, 'r') as nombre_archivo:
        for linea in nombre_archivo:
            lineas += 1
            for palabra in linea.split():
                palabras += 1
            for caracter in linea:
                caracteres += 1
    print('Cantidad de líneas:', lineas)
    print('Cantidad de palabras:', palabras)
    print('Cantidad de caracteres:', caracteres)