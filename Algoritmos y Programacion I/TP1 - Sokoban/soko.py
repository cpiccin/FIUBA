CAJA_FUERA_OBJETIVO = '$'
PARED = '#'
JUGADOR = '@'
OBJETIVO = '.'
OBJETIVO_Y_CAJA = '*'
OBJETIVO_Y_JUGADOR = '+'
CASILLERO_VACIO = ' '


def crear_grilla(desc): 
    '''Crea una grilla a partir de la descripción del estado inicial.

    La descripción es una lista de cadenas, cada cadena representa una
    fila y cada caracter una celda. Los caracteres pueden ser los siguientes:

    Caracter  Contenido de la celda
    --------  ---------------------
           #  Pared
           $  Caja
           @  Jugador
           .  Objetivo
           *  Objetivo + Caja
           +  Objetivo + Jugador'''
    grilla = []
    for cadena in desc:
        grilla.append(list(cadena))
    return grilla


def dimensiones(grilla):
    '''Devuelve una tupla con la cantidad de columnas y filas de la grilla.'''
    return (len(grilla[0]), len(grilla)) # c = len(grilla[0]) y f = len(grilla)


def hay_pared(grilla, c, f):
    '''Devuelve True si hay una pared en la columna y fila (c, f).'''
    return PARED == grilla[f][c]


def hay_objetivo(grilla, c, f):
    '''Devuelve True si hay un objetivo en la columna y fila (c, f).'''
    return grilla[f][c] in (OBJETIVO_Y_JUGADOR, OBJETIVO_Y_CAJA, OBJETIVO)


def hay_caja(grilla, c, f):
    '''Devuelve True si hay una caja en la columna y fila (c, f).'''
    return grilla[f][c] in (CAJA_FUERA_OBJETIVO, OBJETIVO_Y_CAJA)


def hay_jugador(grilla, c, f):
    '''Devuelve True si el jugador está en la columna y fila (c, f).'''
    return grilla[f][c] in (JUGADOR, OBJETIVO_Y_JUGADOR)


def juego_ganado(grilla):
    '''Devuelve True si el juego está ganado.'''
    for f in grilla:
        if CAJA_FUERA_OBJETIVO in f:
            return False
    return True


def posicion_jugador(grilla):
    '''Devuelve en que columna y fila (c, f) esta el jugador.'''
    for f in range(len(grilla)):
        for c in range(len(grilla[f])):
            if grilla[f][c] in (JUGADOR, OBJETIVO_Y_JUGADOR):
                return (c, f)


def movimiento_valido(grilla, direccion, c, f):
    '''Devuelve True si el movimiento en la direccion esta permitido, False si esta bloqueado. 
       El paso esta bloqueado si en la direccion del movimiento hay una pared, una pared y una caja o dos cajas seguidas.'''
    c1, f1 = c+direccion[0], f+direccion[1]
    c2, f2 = c1+direccion[0], f1+direccion[1]
    return (hay_caja(grilla, c1, f1) and hay_pared(grilla, c2, f2)) or (hay_caja(grilla, c1, f1) and hay_caja(grilla, c2, f2)) or hay_pared(grilla, c1, f1)


def define_movimientos(grilla, direccion, c, f):
    '''Modifica la grilla a partir del movimiento ingresado y de la posicion actual del jugador'''
    c1, f1 = c+direccion[0], f+direccion[1]
    c2, f2 = c1+direccion[0], f1+direccion[1]
    
    if hay_objetivo(grilla, c, f) and hay_caja(grilla, c1, f1):
        if hay_objetivo(grilla, c2, f2): # + $ .
            grilla[f2][c2], grilla[f1][c1], grilla[f][c] = OBJETIVO_Y_CAJA, JUGADOR, OBJETIVO
            return
        if hay_objetivo(grilla, c1, f1) and hay_objetivo(grilla, c2, f2): # + * .
            grilla[f2][c2], grilla[f1][c1], grilla[f][c] = OBJETIVO_Y_CAJA, OBJETIVO_Y_JUGADOR, OBJETIVO
            return
        if hay_objetivo(grilla, c1, f1): # + * 
            grilla[f2][c2], grilla[f1][c1], grilla[f][c] = CAJA_FUERA_OBJETIVO, OBJETIVO_Y_JUGADOR, CASILLERO_VACIO
            return
        grilla[f1][c2], grilla[f1][c1], grilla[f][c] = OBJETIVO, JUGADOR, CAJA_FUERA_OBJETIVO # + $ ' '
        return 
    if hay_caja(grilla, c1, f1):
        if hay_objetivo(grilla, c1, f1) and hay_objetivo(grilla, c2, f2): # @ * .
            grilla[f2][c2], grilla[f1][c1], grilla[f][c] = OBJETIVO_Y_CAJA, OBJETIVO_Y_JUGADOR, CASILLERO_VACIO
            return
        if hay_objetivo(grilla, c2, f2): # @ $ .
            grilla[f2][c2], grilla[f1][c1], grilla[f][c] = OBJETIVO_Y_CAJA, JUGADOR, CASILLERO_VACIO
            return
        if hay_objetivo(grilla, c1, f1): # @ * 
            grilla[f2][c2], grilla[f1][c1], grilla[f][c] = CAJA_FUERA_OBJETIVO, OBJETIVO_Y_JUGADOR, CASILLERO_VACIO
            return
        grilla[f2][c2], grilla[f1][c1], grilla[f][c] = CAJA_FUERA_OBJETIVO, JUGADOR, CASILLERO_VACIO # @ $ ' '
        return

    if hay_objetivo(grilla, c1, f1): # @ . ' '
        grilla[f1][c1], grilla[f][c] = OBJETIVO_Y_JUGADOR, CASILLERO_VACIO
        return
    if hay_objetivo(grilla, c, f): # + ' ' ' '
        grilla[f1][c1], grilla[f][c] = JUGADOR, OBJETIVO
        return

    grilla[f1][c1], grilla[f][c] = JUGADOR, CASILLERO_VACIO # @ ' ' ' '
    return
    

def mover(grilla, direccion):
    '''Mueve el jugador en la dirección indicada.

    La dirección es una tupla con el movimiento horizontal y vertical. Dado que
    no se permite el movimiento diagonal, la dirección puede ser una de cuatro
    posibilidades:

    direccion  significado
    ---------  -----------
    (-1, 0)    Oeste
    (1, 0)     Este
    (0, -1)    Norte
    (0, 1)     Sur

    La función debe devolver una grilla representando el estado siguiente al
    movimiento efectuado. La grilla recibida NO se modifica; es decir, en caso
    de que el movimiento sea válido, la función devuelve una nueva grilla.'''
    grilla_actual = [] 
    for x in grilla:
        fila_x = []
        for e in x:
            fila_x.append(e)
        grilla_actual.append(fila_x)
    c, f = posicion_jugador(grilla_actual)
    if movimiento_valido(grilla_actual, direccion, c, f)!=True:
        define_movimientos(grilla_actual, direccion, c, f)
    return grilla_actual