from modelo_Pila import Pila

def validar(expresion):
	pila = Pila()
	for c in expresion:
		if c in '([{':
			pila.apilar(c)
		elif c in ')]}':
			if pila.esta_vacia():
				return False
			tope = pila.desapilar()
			if c == ')' and tope != '(':
				return False
			if c == ']' and tope != '[':
				return False
			if c == '}' and tope != '{':
				return False
	return pila.esta_vacia()
