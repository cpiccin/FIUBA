NOMBRES = ('Candela', 'Olga', 'Lucia', 'Hector', 'Don Jose', 'Jose de San Martin', 'Karina', 'Azucena', 'Fabricio', 'Lucas', 'Aaron')
NOMBRES_GENERO = (('Candela', 'F'), ('Olga', 'F'), ('Lucia', 'F'), ('Hector', 'M'), ('Don Jose', 'M'), ('Jose de San Martin', 'M'), ('Karina', 'F'), ('Azucena', 'F'), ('Fabricio', 'M'), ('Lucas', 'M'),('Aaron', 'M'))
POSICION = 0
CANTIDAD = 3
# a) Recibe una tupla con nombres y para cada nombre imprime el mensaje....

def imprime_mensaje(tupla):
	for nombre in tupla:
		print(f'Estimado {nombre}, vote por mi')


# b) Recibe una tupla con nombres, una posición de origen p y una cantidad n, e imprima el mensaje anterior para los n nombres que se encuentran a partir de la posición p

def imprime_mensaje_v2(tupla, p, n):
	for nombre in tupla[p:p+n]:
		print(f'Estimado {nombre}, vote por mi')


# c) Ahora tiene en cuenta el genero de la persona

def imprime_mensaje_v3(tupla):
	for p in tupla:
		if 'F' in p:
			print(f'Estimada {p[0]}, vote por mi')
		if 'M' in p:
			print(f'Estimado {p[0]}, vote por mi')


