
cumples = {'Candela':'02/01/03'}

regalos = {'Candela':'flores', 'Ivan':'Barbie', 'Pepita':'guitarra','Azucena':'paco'}

precios = {'flores': 15,'Barbie':200, 'guitarra':1250, 'paco':980}


def precios_mes(cumpleaños, regalos, precios):
	res = {}
	for nombre, fecha in cumpleaños.items():
		mes = fecha.split('/')[1]
		regalo = regalos[nombre]
		if mes in res:
			res[mes] += precios[regalo]
			continue
		res[mes] = res.get(mes, precios[regalo])
	return res


print(precios_mes(cumples, regalos, precios))
