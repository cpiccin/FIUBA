from Pila import Pila

def insertar_ordenado(pila, e):
	if pila.esta_vacia() or pila.ver_tope() < e:
		pila.apilar(e)
		return
	otro = pila.desapilar()
	insertar_ordenado(pila, e)
	pila.apilar(otro)

def ordenar_pila(pila):
	if pila.esta_vacia():
		return
	e = pila.desapilar()
	ordenar_pila(pila)
	insertar_ordenado(pila, e)


p1 = Pila()
p1.apilar(3)
p1.apilar(5)
p1.apilar(1)
p1.apilar(4)
p1.apilar(2)
print(p1)

ordenar_pila(p1)

print(p1)
