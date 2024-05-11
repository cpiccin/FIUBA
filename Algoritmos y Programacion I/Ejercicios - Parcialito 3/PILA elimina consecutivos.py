from Pila import Pila

def elimina_consecutivos(pila):
	aux = Pila()
	while not pila.esta_vacia():
		dato = pila.desapilar()
		if not aux.tope or aux.tope.dato != dato:
			aux.apilar(dato)
	while not aux.esta_vacia():
		dato = aux.desapilar()
		pila.apilar(dato)


p1 = Pila()
p1.apilar(1)
p1.apilar(3)
p1.apilar(3)
p1.apilar(6)
p1.apilar(5)
p1.apilar(2)
p1.apilar(3)
p1.apilar(3)
print(p1)
elimina_consecutivos(p1)
print(p1)