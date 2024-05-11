def claves(lista):
	dic = {}
	for tupla in lista:
		valor = [tupla[1]]
		if tupla[0] in dic:
			dic[tupla[0]].append(tupla[1])
			continue
		dicc[tupla[0]] = valor
	return dic 

print(claves( [ ('Hola', 'don Pepito'), ('Hola', 'don Jose'),
('Buenos', 'días') ]))
