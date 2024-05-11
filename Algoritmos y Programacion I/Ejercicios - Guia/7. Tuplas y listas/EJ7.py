DATOS = [('Piccin', 'Candela', '0'), ('Benlloch', 'Agustin', 'I'), ('Piccin', 'Claudio', 'B'), ('Gelabert', 'Elsa', 'T')]

def lista(datos):  #Nombre Inicial. Apellido
	lista_final = []
	for tupla in datos:
		lista_final.append(f'{tupla[1]} {tupla[2]}. {tupla[0]}')
	return lista_final


