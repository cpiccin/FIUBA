def contar_apariciones(lista,elemento):
    '''Dada una lista desordenada y un elemento, devuelve la cantidad de veces que aparece el elemento en la lista'''
    cantidad = 0
    for e in lista:
        if e == elemento:
            cantidad += 1
    return cantidad