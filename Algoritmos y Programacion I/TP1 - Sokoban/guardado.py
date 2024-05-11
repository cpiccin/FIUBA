desc = [
        '######',
        '#  @ #',
        '######', ]
ESTE = (1, 0)
GRILLA = crear_grilla(desc)
print(GRILLA)
print(mover(GRILLA, (-1, 0)))


CAJA_FUERA_OBJETIVO = '$'
PARED = '#'
JUGADOR = '@'
OBJETIVO = '.'
OBJETIVO_Y_CAJA = '*'
OBJETIVO_Y_JUGADOR = '+'



def define_movimientos(grilla, direccion, c, f):
    '''Modifica la grilla a partir del movimiento ingresado y de la posicion actual del jugador'''
    c1, f1 = c+direccion[0], f+direccion[1]
    c2, f2 = c1+direccion[0], f1+direccion[1]          
#                                                                               Posibles movimientos
#                                                                              ----------------------
    if hay_objetivo(grilla, c, f) and hay_caja(grilla, c1, f1):
        if hay_objetivo(grilla, c1, f1) and hay_objetivo(grilla, c2, f2):       # + * . ----> . + *
            grilla[f2][c2] = OBJETIVO_Y_CAJA
            grilla[f1][c1] = OBJETIVO_Y_JUGADOR
            grilla[f][c] = OBJETIVO 
            return
        if hay_objetivo(grilla, c2, f2):                                        # + $ . ----> . @ *
            grilla[f2][c2] = OBJETIVO_Y_CAJA
            grilla[f1][c1] = JUGADOR
            grilla[f][c] = OBJETIVO
            return
        if hay_objetivo(grilla, c1, f1):                                        # + * ' ' ----> . + $
            grilla[f2][c2] = CAJA_FUERA_OBJETIVO
            grilla[f1][c1] = OBJETIVO_Y_JUGADOR
            grilla[f][c] = OBJETIVO
            return
        grilla[f2][c2] = CAJA_FUERA_OBJETIVO                                    # + $ ' ' ----> . @ $
        grilla[f1][c1] = JUGADOR 
        grilla[f][c] = OBJETIVO
        return 
    if hay_caja(grilla, c1, f1):
        if hay_objetivo(grilla, c1, f1) and hay_objetivo(grilla, c2, f2):       # @ * . ----> ' ' + *
            grilla[f2][c2] = OBJETIVO_Y_CAJA
            grilla[f1][c1] = OBJETIVO_Y_JUGADOR
            grilla[f][c] = CASILLERO_VACIO
            return
        if hay_objetivo(grilla, c2, f2):                                        # @ $ . ----> ' ' @ *
            grilla[f2][c2] = OBJETIVO_Y_CAJA
            grilla[f1][c1] = JUGADOR
            grilla[f][c] = CASILLERO_VACIO
            return
        if hay_objetivo(grilla, c1, f1):                                        # @ * ' ' ----> ' ' + $
            grilla[f2][c2] = CAJA_FUERA_OBJETIVO
            grilla[f1][c1] = OBJETIVO_Y_JUGADOR
            grilla[f][c] = CASILLERO_VACIO
            return
        grilla[f2][c2] = CAJA_FUERA_OBJETIVO                                    # @ $ ' ' ----> ' ' @ $
        grilla[f1][c1] = JUGADOR
        grilla[f][c] = CASILLERO_VACIO
        return
    if hay_objetivo(grilla, c1, f1):                                            # @ . ' ' ----> ' ' + ' '
        grilla[f1][c1] = OBJETIVO_Y_JUGADOR
        grilla[f][c] = CASILLERO_VACIO
        return
    if hay_objetivo(grilla, c, f):                                              # + ' ' ' ' ----> . @ ' '
        grilla[f1][c1] = JUGADOR
        grilla[f][c] = OBJETIVO
        return
    grilla[f1][c1] = JUGADOR                                                    # @ ' ' ' ' ----> ' ' @ ' '
    grilla[f][c] = CASILLERO_VACIO
    return

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