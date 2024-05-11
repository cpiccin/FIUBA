def maximo(numeros):
    '''
    Devuelve el valor máximo de la lista de números
    '''
    maximo = 0
    if len(numeros)==0:
        return None
    for n in numeros:
        if n > maximo:
            maximo = n
    return maximo



def maximo_y_posicion(numeros):
    '''
    Devuelve una tupla con el valor máximo de la lista de números y su posición
    '''
    maximo = 0
    pos = -1
    pos_maximo = 0
    if len(numeros)==0:
            return (None, pos)
    for n in numeros:
        pos += 1
        if n > maximo:
            maximo = n
            pos_maximo = pos
    return (maximo, pos_maximo)


print(maximo_y_posicion([]))