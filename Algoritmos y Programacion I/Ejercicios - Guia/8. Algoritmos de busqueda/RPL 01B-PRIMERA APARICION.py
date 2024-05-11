def buscar_primera_aparicion(lista, elemento):
    '''Dada una lista y un elemento, devuelve la primera aparicion del elemento en la lista, si no aparece en la lista devuelve -1'''
    if not elemento in lista:
        return -1
    return lista.index(elemento)