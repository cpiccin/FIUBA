class _Nodo:
    def __init__(self, dato, prox=None):
        self.dato = dato
        self.prox = prox

class Cola:

    def __init__(self):
        self.primero = None
        self.ultimo = None

    def encolar(self, x):
        nuevo = _Nodo(x)
        if self.ultimo is not None:
            self.ultimo.prox = nuevo
            self.ultimo = nuevo
        else:
            self.primero = nuevo
            self.ultimo = nuevo

    def desencolar(self):
        if self.primero is None:
            raise ValueError("La cola está vacía")
        valor = self.primero.dato
        self.primero = self.primero.prox
        if not self.primero:
            self.ultimo = None
        return valor

    def esta_vacia(self):
        return self.primero is None


class TorreDeControl:

    def __init__(self):
        self.despegando = Cola()
        self.aterrizando = Cola()

    def nuevo_arribo(self, avion):
        self.aterrizando.encolar(avion)

    def nueva_partida(self, avion):
        self.despegando.encolar(avion)

    def ver_estado(self):
        l_despegando = 'Vuelos esperando para despegar: '
        act = self.despegando.primero
        while act:
            l_despegando += act.dato
            act = act.prox
        l_aterrizando = 'Vuelos esperando para aterrizar: '
        act = self.aterrizando.primero
        while act:
        	if act.prox:
        		l_aterrizando += act.dato + ', '
        	else:
        		l_aterrizando += act.dato
        	act = act.prox
        print(l_aterrizando)
        print(l_despegando)

    def asignar_pista(self):
        if self.aterrizando.primero == None and self.despegando.primero == None:
            print('No hay vuelos en espera')
            return
        if not self.aterrizando.primero:
            print(f'El vuelo {self.despegando.primero.dato} despego con exito')
            self.despegando.desencolar()
        else:
            print(f'El vuelo {self.aterrizando.primero.dato} aterrizo con exito')
            self.aterrizando.desencolar()


torre = TorreDeControl()
torre.nuevo_arribo('AR156')
torre.nueva_partida('KLM1267')
torre.nuevo_arribo('AR32')
torre.ver_estado()

torre.asignar_pista()
torre.asignar_pista()

torre.asignar_pista()

torre.asignar_pista()