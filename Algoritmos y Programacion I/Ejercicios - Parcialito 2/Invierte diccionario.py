def invierte(dic):

	res = {}

	for clave, lista in dic.items():
		for n in lista:
			if n in res:
				res[n].append(clave)
				continue
			res[n] = res.get(n, [clave])
	return res 



d = {"clave_1": [1,2,3], "clave_2": [4,6], "clave_3": [1,4]}
 
print(invierte(d))