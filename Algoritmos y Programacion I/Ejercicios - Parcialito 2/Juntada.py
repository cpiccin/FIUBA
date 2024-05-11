def juntada(amigos):

	dias_comunes = []

	for amigo in amigos:
		dias_comunes = amigos[amigo]
		break

	for amigo in amigos:

		for dia in dias_comunes:
			if dia not in amigos[amigo]:
				dias_comunes.pop(dias_comunes.index(dia))

	return dias_comunes


amigos = {'Juan':['MIE', 'VIE', 'SAB'], 'Jose':['VIE', 'SAB', 'DOM'], 'Jorge':['JUE', 'VIE', 'SAB']}

print(juntada(amigos))	 



