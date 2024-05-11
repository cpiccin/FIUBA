def agrupa(dics):
	res = {}

	for dic in dics:
		for clave in dic:
			if clave in res:
				res[clave].append(dic[clave])
				continue
			res[clave] = res.get(clave, [dic[clave]])
	return res 


dics = [{"clave_1": 1, "clave_2": 2, "clave_3": 3},
 {"clave_1": 4, "clave_3": 5},
 {"clave_4": 6, "clave_3": 7, "clave_2": 8}]
 

print(agrupa(dics))