import gamelib
ANCHO_VENTANA = 300
ALTO_VENTANA = 390
DIM = 10 # cantidad de filas y columnas
DIM_CASILLEROS = 30 # tamaño de los casilleros
JUGADORES = ['X', 'O']

def juego_crear():
    '''Devuelve una estructura (lista de listas) que representa el tablero inicial'''
    fila = [' ' for x in range(DIM)]
    tablero = []
    for _ in range(DIM):
        tablero.append(fila[:])
    return tablero

def juego_actualizar(juego, x, y, turno):
    '''Actualizar el estado del juego

    x e y son las coordenadas (en pixels) donde el usuario hizo click.
    Esta función determina si esas coordenadas corresponden a una celda
    del tablero; en ese caso determina el nuevo estado del juego y lo
    devuelve'''
    if y < DIM_CASILLEROS*DIM and x < DIM_CASILLEROS*DIM:
        for i in range(DIM):
            for j in range(DIM):
                if (DIM_CASILLEROS*j<x<DIM_CASILLEROS*(j+1)) and (DIM_CASILLEROS*i<y<DIM_CASILLEROS*(i+1)):
                    if juego[i][j] == ' ':
                        juego[i][j] = turno
                        turno_siguiente = siguiente_turno(JUGADORES.index(turno))
                        return juego, turno_siguiente   
    return juego, turno

def siguiente_turno(turno_actual):
    '''Recibe el turno que modifico por ultimo el estado del juego.
       Devuelve el proximo turno correspondiente.'''
    if turno_actual == 0:
        return JUGADORES[1]
    return JUGADORES[0]

def juego_mostrar(juego, turno):
    '''Muestra graficamente los eventos del juego a medida que se actualiza el estado del mismo'''
    gamelib.draw_image('fondo.gif', 0, 0)
    gamelib.draw_rectangle(0, DIM_CASILLEROS*DIM, ANCHO_VENTANA, ALTO_VENTANA, outline='white', fill='white')
    gamelib.draw_text('5 en linea', ANCHO_VENTANA//2, ALTO_VENTANA-2*DIM_CASILLEROS, size=16, font='Comic Sans MS', fill='#000000', bold=True)
    gamelib.draw_text(f'Turno de {turno}', ANCHO_VENTANA//2, ALTO_VENTANA-DIM_CASILLEROS, size=14, font='Comic Sans MS', fill='#000000')
    for i in range(DIM):
        for j in range(DIM):
            gamelib.draw_rectangle(DIM_CASILLEROS*j, DIM_CASILLEROS*i, DIM_CASILLEROS*(j+1), DIM_CASILLEROS*(i+1), outline='#000000', fill='', width=1)
            for turno in juego[i][j]:
                    gamelib.draw_text(turno, (DIM_CASILLEROS*j + DIM_CASILLEROS*(j+1))//2, (DIM_CASILLEROS*i + DIM_CASILLEROS*(i+1))//2, size=14, font='Verdana', fill='#FF4600', bold=True)

def main():
    
    juego = juego_crear()
    turno = choice(JUGADORES)
    contador = JUGADORES.index(turno)
    
    gamelib.resize(ANCHO_VENTANA, ALTO_VENTANA)

    while gamelib.is_alive():

        gamelib.draw_begin()
        juego_mostrar(juego, turno)
        gamelib.draw_end()

        ev = gamelib.wait()

        if not ev:
            break

        if ev.type == gamelib.EventType.KeyPress and ev.key == 'Escape':
            break

        if ev.type == gamelib.EventType.ButtonPress:
            x, y = ev.x, ev.y 
            juego, turno = juego_actualizar(juego, x, y, turno)
            

gamelib.init(main)