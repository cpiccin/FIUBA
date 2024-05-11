def buscar_primera_aparicion(lista, elemento):
    '''Dada una lista y un elemento, devuelve la primera aparicion del elemento en la lista, si no aparece en la lista devuelve -1'''
    if not elemento in lista:
        return -1
    return lista.index(elemento)

def buscar_apariciones(lista, elemento):
    '''Dada una lista y un elemento, busca todos los elementos que coincidan con el pasado por parámetro y devuelva una lista con las posiciones.'''
    posiciones = []
    while buscar_primera_aparicion(lista, elemento)!=-1:
        pos = buscar_primera_aparicion(lista, elemento)
        lista.pop(pos)
        lista.insert(pos, 'x')
        posiciones.append(pos)
    return posiciones