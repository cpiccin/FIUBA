def actores(archivo_csv):
	'''[peli; anio; [actor1, actor2] ]'''
	res = {}
	with open(archivo_csv) as f:
		next(f)

		for linea in f:
			linea = linea.rstrip('\n').split(';')
			if not linea[0] or not linea[1] or not linea[2]:
				continue
			if not linea[1].isdigit():
				continue
			for actor in linea[2].split(','):
				res[actor] = res.get(actor, [])
				res[actor].append(int(linea[1]))

	return res 


for actor in actores('actores.csv'):
	print(actor, actores('actores.csv')[actor])