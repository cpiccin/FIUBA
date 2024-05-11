import gamelib
import soko
import csv 
from pila import Pila 

DIRECCIONES = {'ESTE': (1,0), 'OESTE': (-1, 0), 'NORTE': (0, -1), 'SUR': (0, 1), 'REINICIAR': 'REINICIAR', 'SALIR':'SALIR', 'REHACER': 'REHACER', 'DESHACER': 'DESHACER', 'PISTA':'PISTA'} 
ANCHO_VENTANA = 300
ALTO_VENTANA = 300
DIM_IMG = 32
SENTIDOS = {(1,0), (-1, 0), (0, -1), (0, 1)}

def carga_teclas_validas(archivo_teclas):
    '''Dado un archivo de teclas validas y su efecto en el estado del juego
       devuelve un diccionario con esta informacion'''
    with open(archivo_teclas) as teclas:
        teclas_validas = {}
        for linea in csv.reader(teclas, delimiter='='):
            if linea == []:
                continue
            teclas_validas[linea[0].rstrip(' ')] = linea[1].lstrip(' ')
        return teclas_validas


def carga_niveles(archivo_niveles):
    '''Dado un archivo con niveles devuelve una lista ordenada por nivel, 
       del primero al ultimo, con las descripciones de los mismos'''
    with open(archivo_niveles) as niveles:
        
        nivel_desc = []
        lista_niveles = []
        max_len = 0
        for linea in niveles:

            if 'Level' in linea or "'" in linea: # solo guarda las desc
                continue

            if linea == '\n':
                if len(nivel_desc) == 0:
                    continue
                lista_niveles.append(agrega_casillero_vacio(nivel_desc, max_len))
                nivel_desc, max_len = [], 0
                continue

            if max_len < len(linea):
                max_len = len(linea)

            nivel_desc.append(linea.rstrip())

        if len(nivel_desc) > 0:
            lista_niveles.append(agrega_casillero_vacio(nivel_desc, max_len))

        return list(lista_niveles)


def agrega_casillero_vacio(desc, max_len):
    '''Agrega el caracter correspondiente a un casillero vacio a cada linea
       de forma que quede una descripcion de nivel cuadrada, de dimensiones
       NxN'''
    for i in range(len(desc)):
        if len(desc[i]) < max_len:
            desc[i] += soko.CASILLERO_VACIO*(max_len-len(desc[i])-1) 
    return desc
    

def dibuja_juego(juego, solucion):
    '''Dibuja en un ventana el estado actual del juego'''
    ancho, alto = soko.dimensiones(juego)
    ANCHO_VENTANA, ALTO_VENTANA = ancho*DIM_IMG, alto*DIM_IMG
    gamelib.resize(ANCHO_VENTANA, ALTO_VENTANA) 
    
    for i in range(ancho):
        for j in range(alto):
            if solucion: # avisa si hay pistas disponibles
                gamelib.draw_text('Pistas disponibles', ANCHO_VENTANA//2, DIM_IMG//2, size=14, font='Helvetica', fill='#3FB50F', bold=True)
            if solucion == False: # avisa si no hay pistas disponibles
                gamelib.draw_text('NO hay pistas disponibles', ANCHO_VENTANA//2, DIM_IMG//2, size=13, font='Helvetica', fill='red', bold=True)
            gamelib.draw_image('ground.gif', DIM_IMG*i, DIM_IMG*j)
            if soko.hay_pared(juego, i, j):
                gamelib.draw_image('wall.gif', DIM_IMG*i, DIM_IMG*j)
            if soko.hay_objetivo(juego, i,j):
                gamelib.draw_image('goal.gif', DIM_IMG*i, DIM_IMG*j)
            if soko.hay_caja(juego, i, j):
                gamelib.draw_image('box.gif', DIM_IMG*i, DIM_IMG*j)
            if soko.hay_jugador(juego, i, j):
                gamelib.draw_image('player.gif', DIM_IMG*i, DIM_IMG*j)


def generar_pilas(juego):
    '''Genera las pilas deshacer y rehacer, deshacer inicializada con el estado inicial del juego'''
    pila_deshacer = Pila()
    pila_rehacer = Pila()
    return [pila_deshacer, pila_rehacer]


def actualiza_juego(juego_actual, direccion, pilas, conjunto_pistas): 
    '''Actualiza el juego segun la instruccion recibida'''
    if direccion == 'DESHACER':
        conjunto_pistas = None, []
        juego_actual = deshacer(juego_actual, pilas)

    elif direccion == 'REHACER':
        conjunto_pistas = None, []
        juego_actual = rehacer(juego_actual, pilas)

    elif direccion == 'PISTA':
        juego_actual, conjunto_pistas = pista(juego_actual, conjunto_pistas, pilas)

    else:
        pilas[0].apilar(juego_actual)
        conjunto_pistas = None, []
        pilas[1] = Pila() 
        juego_actual = soko.mover(juego_actual, direccion)

    return juego_actual, conjunto_pistas


def pista(juego, conjunto_pistas, pilas):
    '''Determina como se comporta la grilla con la instruccion PISTA'''
    if conjunto_pistas[0]:
        direccion = conjunto_pistas[1].pop(0)
        juego = soko.mover(juego, direccion)
        pilas[1] = Pila()
        pilas[0].apilar(juego)
    else:
        conjunto_pistas = buscar_solucion(juego)
    return juego, conjunto_pistas


def deshacer(juego, pilas):
    '''Determina como se comporta la grilla con la instruccion DESHACER'''
    if pilas[0].esta_vacia():
        pilas[0].apilar(juego)
        return juego
    juego = pilas[0].desapilar()
    pilas[1].apilar(juego)
    return juego


def rehacer(juego, pilas):
    '''Determina como se comporta la grilla con la instruccion REHACER'''
    if pilas[1].esta_vacia():
        return juego 
    juego = pilas[1].desapilar()
    pilas[0].apilar(juego)
    return juego


def buscar_solucion(juego):
    '''Dado el estado actual del juego devuelve si hay pistas disponibles y una lista que contiene 
       direcciones las cuales tiene que seguir el jugador para completar el nivel'''
    visitados = set({})
    return backtrack(juego, visitados)
    

def backtrack(juego, visitados):
    '''Algoritmo de backtracking para encontrar una solucion al nivel'''
    visitados.add(inmutable(juego))
    if soko.juego_ganado(juego):
        return True, []
    for accion in SENTIDOS:
        nuevo_juego = soko.mover(juego, accion)
        if inmutable(nuevo_juego) in visitados:  
            continue        
        solucion_encontrada, acciones = backtrack(nuevo_juego, visitados)
        if solucion_encontrada:
            return True, ([accion]+acciones)
    return False, None


def inmutable(juego): 
    '''Funcion auxiliar para backtrack. Convierte en tupla de cadenas a la desc del juego'''
    res = ()
    for lista in juego:
        cad = ''.join(lista)
        res += (cad,)
    return res


def main():
    
    niveles, teclas_validas, nivel_actual = carga_niveles('niveles.txt'), carga_teclas_validas('teclas.txt'), 0
    juego_actual = soko.crear_grilla(niveles[nivel_actual])
    pilas = generar_pilas(juego_actual)
    conjunto_pistas = None, [] # disponibilidad de pistas/lista de pistas a seguir

    gamelib.resize(ANCHO_VENTANA, ALTO_VENTANA)

    while gamelib.is_alive():
            
        gamelib.draw_begin()
        dibuja_juego(juego_actual, conjunto_pistas[0])
        gamelib.draw_end()

        ev = gamelib.wait(gamelib.EventType.KeyPress)
        if not ev:
            break

        tecla = ev.key
        
        if tecla in teclas_validas:
            
            direccion = DIRECCIONES[teclas_validas[tecla]]
            
            if direccion == 'SALIR':
                break
            if direccion == 'REINICIAR':
                conjunto_pistas = None, []
                juego_actual = niveles[nivel_actual]
                continue
            
            juego_actual, conjunto_pistas = actualiza_juego(juego_actual, direccion, pilas, conjunto_pistas)
           
            if soko.juego_ganado(juego_actual): 
                conjunto_pistas = None, []
                nivel_actual += 1
                if nivel_actual >= len(niveles):
                    break # se completaron todos los niveles disponibles
                juego_actual, pilas = soko.crear_grilla(niveles[nivel_actual]), generar_pilas(juego_actual) 

        else:
            continue

    
gamelib.init(main)