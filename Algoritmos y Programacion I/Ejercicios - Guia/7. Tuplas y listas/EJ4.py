# a) Recibe dos vectores como tuplas y devuelve su producto escalar

def producto_escalar(vector1, vector2):
	suma = 0
	for n in range(len(vector1)):
		suma += vector1[n]*vector2[n]
	return suma

# b) Recibe dos vectores y devuelve si son ortogonales o no

def son_ortogonales(vector1, vector2):
	if producto_escalar(vector1, vector2) == 0:
		return True
	return False

# c) Dados dos vectores devuelve si son paralelos o no

# d) Dado un vector devuelve su norma
