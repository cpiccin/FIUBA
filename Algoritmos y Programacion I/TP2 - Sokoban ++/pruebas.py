import gamelib
import soko
import csv 

ANCHO_VENTANA = 300
ALTO_VENTANA = 300


def define_teclas(archivo_teclas, tecla):
    '''Recibe el nombre de un archivo con las teclas que controlan el juego y la tecla ingresada.
       Si la tecla no es parte de los controles no realiza ninguna accion, si es valida en caso de ser una tecla 
       que modifica la posicion devuelve la direccion en la que se tiene que mover y si no, devuelve la tecla que 
       realizo determinada accion (se REINICIO con 'r', se SALIO con 'Escape').'''
    direcciones = {'ESTE': (1,0), 'OESTE': (-1, 0), 'NORTE': (0, -1), 'SUR': (0, 1), 'REINICIAR': 'r', 'SALIR':'Escape'}
    teclas_validas = []
    direccion = None
    with open(archivo_teclas) as teclas:
        
        for linea in csv.reader(teclas, delimiter='='):
            if linea == []:
                continue
            teclas_validas.append(linea[0].rstrip(' '))
            if tecla == linea[0].rstrip(' '):
                direccion = direcciones[linea[1].lstrip(' ')]
        
        if tecla not in teclas_validas:
            return False
        
        return direccion


def lista_niveles(archivo_niveles):
    '''Dado el nombre de un archivo que contiene niveles devuelve una lista con todos los niveles.'''
    lista_niveles = [[]]
    nivel_desc = []
    nivel_titulo = ''
    with open(archivo_niveles) as niveles:
        
        for linea in niveles:
            if 'Level' in linea:
                nivel_titulo = linea.rstrip()
                continue
            if "'" in linea:
                nivel_titulo += f': {linea.rstrip()}'
                continue
            if linea == '\n':
                lista_niveles.append((nivel_titulo, nivel_desc))
                nivel_desc = []
                nivel_titulo = ""
                continue
            nivel_desc.append(linea.rstrip())
        
        if (nivel_titulo, nivel_desc) not in lista_niveles:
            lista_niveles.append((nivel_titulo, nivel_desc))

        return lista_niveles


def proximo_nivel(niveles, nivel_actual):
    '''Segun la posicion del nivel resuelto en la lista de niveles, devuelve el proximo nivel correspondiente.
       En caso de ser el ultimo nivel de la lista devuelve False.'''
    nivel_completado = niveles.index(nivel_actual)
    if nivel_completado == (len(niveles)-1):
        return False
    return niveles[nivel_completado+1]


def dibuja_juego(juego):
    '''Muestra en una ventana el estado del juego actual
    .'''
    mayor_len = 0
    for fila in juego:
        if len(fila) > mayor_len:
            mayor_len = len(fila)

    ancho, alto = soko.dimensiones(juego)
    ANCHO_VENTANA, ALTO_VENTANA = mayor_len*32, alto*32
    gamelib.resize(ANCHO_VENTANA, ALTO_VENTANA) 
    
    for i in range(mayor_len):
        for j in range(alto):
            gamelib.draw_image('ground.gif', 32*i, 32*j)

            try:
                if soko.hay_pared(juego, i, j):
                    gamelib.draw_image('wall.gif', 32*i, 32*j)
                if soko.hay_objetivo(juego, i,j):
                    gamelib.draw_image('goal.gif', 32*i, 32*j)
                if soko.hay_caja(juego, i, j):
                    gamelib.draw_image('box.gif', 32*i, 32*j)
                if soko.hay_jugador(juego, i, j):
                    gamelib.draw_image('player.gif', 32*i, 32*j)
            except IndexError:
                gamelib.draw_image('ground.gif', 32*i, 32*j)


def main():

    niveles = lista_niveles('niveles.txt')
    nivel_actual = proximo_nivel(niveles, [])
    juego_actual = soko.crear_grilla(nivel_actual[1])

    gamelib.resize(ANCHO_VENTANA, ALTO_VENTANA)

    while gamelib.is_alive():
            
        gamelib.draw_begin()
        dibuja_juego(juego_actual)
        gamelib.draw_end()

        ev = gamelib.wait(gamelib.EventType.KeyPress)
        if not ev:
            break

        tecla = ev.key
        
        direccion = define_teclas('teclas.txt', tecla)

        if not direccion:
            continue
        
        if direccion == 'r':
            juego_actual = nivel_actual[1]
            continue            

        if direccion == 'Escape':
            break

        juego_actual = soko.mover(juego_actual, direccion)

        if soko.juego_ganado(juego_actual):
            nivel_actual = proximo_nivel(niveles, nivel_actual)
            if not nivel_actual:
                break
            juego_actual = soko.crear_grilla(nivel_actual[1])


gamelib.init(main)