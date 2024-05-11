# Escribir una funcion reducir que reciba por parametro una cola y una funcion f de dos
# parametros, y aplique sucesivamente la funcion f a los dos primeros elementos de la cola (luego
# de desencolarlos) y encole el resultado, hasta que solo quede un elemento. La funcion reducir
# debe devolver el unico elemento restante en la cola

from Cola import Cola, _Nodo

def reducir(cola, f):
	while not cola.esta_vacia():
		a = cola.desencolar()
		if cola.esta_vacia():
			return a
		b = cola.desencolar()
		cola.encolar(f(a,b))
	return cola.primero.dato


def suma(n1, n2):
	return n1+n2


c1 = Cola()
c1.encolar(2)
c1.encolar(2)
c1.encolar(2)
c1.encolar(2)
print(reducir(c1, suma))
