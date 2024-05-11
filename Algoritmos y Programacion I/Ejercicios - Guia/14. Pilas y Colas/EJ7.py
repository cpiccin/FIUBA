from modelo_Cola import Cola

def tail(archivo, n):
	cola = Cola()
	with open(archivo) as archivo:
		for linea in archivo:
			cola.encolar(linea)
			n -= 1 
			if n < 0:
				cola.desencolar()
		for _ in range(n):
			print(cola.primero.dato)
			cola.desencolar()	
