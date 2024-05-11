def leer_dialogo(nombre_archivo):

	res = {}
	with open(nombre_archivo) as dialogo:
		for linea in dialogo:
			linea = linea.rstrip('\n').split(':')
			persona, palabras = linea[0], linea[1].split()

			if persona not in res:
				res[persona] = res.get(persona, {})

			for palabra in palabras:
				if palabra in res[persona]:
					res[persona][palabra] += 1
				res[persona][palabra] = res[persona].get(palabra, 1)

	return res
 
		
		






print(leer_dialogo('Dialogo.txt'))