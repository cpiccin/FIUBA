def estrellas(dic):
	res = {}
	for e in dic:
		if dic[e] in res:
			res[dic[e]].append(e)
			continue
		res[dic[e]] = res.get(dic[e], [e])
	return res 

d = {'La Mazorca': 1, 'Lemonmay': 4, 'Las Cumbres': 4} 
print(estrellas(d))