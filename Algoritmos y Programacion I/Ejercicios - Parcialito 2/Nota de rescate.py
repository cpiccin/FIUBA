def nota(texto, revista):
	letras = {}
	for l in revista.lower():
		if l == ' ':
			continue
		letras[l] = letras.get(l, 0)
		if l in letras:
			letras[l] += 1
			continue
		
	for l in list(texto.lower()):
		if l == ' ' or l not in letras:
			continue
		if l in letras and letras[l] > 0:
			letras[l] -= 1
			continue
		else:
			return False
	return True
		

print(nota('Porotos amargos', 'Algoritmoss y Programacion'))