# Dada una pila con números, escribir una función recursiva que
# calcule el producto de los mismos. La pila debe quedar en su
# estado original al final de la ejecución.

from Pila import Pila


def _calcular_producto(pila, cant):
    if pila.esta_vacia():
        return 1
    dato = pila.desapilar()
    cant += dato * _calcular_producto(pila, cant)
    pila.apilar(dato)
    return cant

def calcular_producto(pila):
    return _calcular_producto(pila, 0)


p1 = Pila()
p1.apilar(1)
p1.apilar(2)
p1.apilar(3)
p1.apilar(4)
p1.apilar(5)
print(p1)
print(calcular_producto(p1))
print(p1)