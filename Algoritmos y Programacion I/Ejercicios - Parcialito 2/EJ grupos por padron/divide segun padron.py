def divide(padrones, grupo1, grupo2, grupo3):
	with open(padrones) as padrones, open(grupo1, 'w') as g1, open(grupo2, 'w') as g2, open(grupo3, 'w') as g3:
		for padron in padrones:
			grupo = int(padron)%3
			if grupo == 0:
				g1.write(padron)
			if grupo == 1:
				g2.write(padron)
			if grupo == 2:
				g3.write(padron)


divide('alumnos.txt', 'grupo1.txt', 'grupo2.txt', 'grupo3.txt')