def partir_tuplas(lista):
    '''Recibe una lista de tuplas de la forma (n, m) y devuelva dos listas.
        La primera tendrá los elementos de la primer posicion de las tuplas
        La segunda, los que estén en la segunda posición.'''
    lista_p1 = []
    lista_p2 = []
    for t in lista:
        lista_p1.append(t[0])
        lista_p2.append(t[1])
    return lista_p1, lista_p2