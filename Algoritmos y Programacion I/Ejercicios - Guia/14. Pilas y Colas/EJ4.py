from modelo_Pila import Pila

class Carta:

    def __init__(self, palo, valor):
        self.palo = palo
        self.valor = valor


class Solitario:

    def __init__(self):
        self.pila = Pila()

    def apilar(self, carta):
        if not self.pila.tope:
            self.pila.apilar(carta)
            return
        carta_anterior = self.pila.tope.dato
        if not (carta_anterior.palo != carta.palo and carta_anterior.valor > carta.valor and carta_anterior.valor-2 < carta.valor):
            raise Exception('Carta inválida')
        else:
            self.pila.apilar(carta)

solitario = Solitario()
solitario.apilar(Carta('Copa', 12))
solitario.apilar(Carta('Oro', 11))
solitario.apilar(Carta('Oro', 10))
solitario.apilar(Carta('Espada', 11))
solitario.apilar(Carta('Copa', 9))
solitario.apilar(Carta('Copa', 10))
