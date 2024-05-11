import gamelib
import soko
import csv 

DIRECCIONES = {'ESTE': (1,0), 'OESTE': (-1, 0), 'NORTE': (0, -1), 'SUR': (0, 1), 'REINICIAR': 'REINICIAR', 'SALIR':'SALIR'} 
ANCHO_VENTANA = 300
ALTO_VENTANA = 300
DIM_IMG = 32

def carga_teclas_validas(archivo_teclas):
        with open(archivo_teclas) as teclas:
            teclas_validas = {}
            for linea in csv.reader(teclas, delimiter='='):
                if linea == []:
                    continue
                teclas_validas[linea[0].rstrip(' ')] = linea[1].lstrip(' ')
            return teclas_validas


def cargar_niveles(archivo_niveles):

    with open(archivo_niveles) as niveles:
        
        nivel_desc = []
        lista_niveles = []
        max_len = 0
        for linea in niveles:

            if 'Level' in linea or "'" in linea: # solo guarda las desc
                continue

            if linea == '\n' and '' not in nivel_desc:
                nivel_desc = agrega_espacios(nivel_desc, max_len)
                lista_niveles.append(nivel_desc)
                nivel_desc, max_len = [], 0
                continue

            if max_len < len(linea):
                max_len = len(linea)

            nivel_desc.append(linea.rstrip())

        return lista_niveles


def agrega_espacios(desc, max_len):
    for i in range(len(desc)):
        if len(desc[i]) < max_len:
            desc[i] += ' '*(max_len-len(desc[i])-1) 
    return desc
    

def dibuja_juego(juego):

    ancho, alto = soko.dimensiones(juego)
    ANCHO_VENTANA, ALTO_VENTANA = ancho*DIM_IMG, alto*DIM_IMG
    gamelib.resize(ANCHO_VENTANA, ALTO_VENTANA) 
    
    for i in range(ancho):
        for j in range(alto):
            gamelib.draw_image('ground.gif', DIM_IMG*i, DIM_IMG*j)
            if soko.hay_pared(juego, i, j):
                gamelib.draw_image('wall.gif', DIM_IMG*i, DIM_IMG*j)
            if soko.hay_objetivo(juego, i,j):
                gamelib.draw_image('goal.gif', DIM_IMG*i, DIM_IMG*j)
            if soko.hay_caja(juego, i, j):
                gamelib.draw_image('box.gif', DIM_IMG*i, DIM_IMG*j)
            if soko.hay_jugador(juego, i, j):
                gamelib.draw_image('player.gif', DIM_IMG*i, DIM_IMG*j)


def main():

    niveles = cargar_niveles('niveles.txt')
    print(niveles)
    teclas_validas = carga_teclas_validas('teclas.txt')
    nivel_actual = 0
    juego_actual = soko.crear_grilla(niveles[nivel_actual])
    
    gamelib.resize(ANCHO_VENTANA, ALTO_VENTANA)

    while gamelib.is_alive():
            
        gamelib.draw_begin()
        dibuja_juego(juego_actual)
        gamelib.draw_end()

        ev = gamelib.wait(gamelib.EventType.KeyPress)
        if not ev:
            break

        tecla = ev.key
        
        if tecla in teclas_validas:
            direccion = DIRECCIONES[teclas_validas[tecla]]
            if direccion == 'REINICIAR':
                juego_actual = niveles[nivel_actual]
                continue            
            if direccion == 'SALIR':
                break
            juego_actual = soko.mover(juego_actual, direccion)
        else:
            continue

        if soko.juego_ganado(juego_actual):
            nivel_actual += 1
            if nivel_actual >= len(niveles): # se llego al ultimo nivel
                break
            juego_actual = soko.crear_grilla(niveles[nivel_actual])


gamelib.init(main)