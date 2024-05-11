canciones = {'Body Paint': 291, 
'Impressions of You': 238, 
'Waterfalls': 280, 
'If I Can Dream': 200, 
'All I Think About Now':187, 
'Come Closer': 179, 
'Regtest': 349,
'Bound 2': 229,
'Sweet Dreams': 217,
'The End Of The World': 224,
'Es un Secreto': 191,
'Public Service Announcement (Interlude)': 166,
'Noko': 210}

listas = {'NO': ['Impressions of You', 'Waterfalls', 'All I Think About Now'], 
'Ayer': ['Sweet Dreams', 'If I Can Dream', 'Noko', 'Bound 2'],
'Barcos': ['Regtest', 'Waterfalls', 'The End Of The World', 'Come Closer', 'Sweet Dreams']}


def duracion(canciones, listas):
	res = {}

	for lista in listas:
		res[lista] = 0 

	for lista in listas:
		for cancion in listas[lista]:
			res[lista] += canciones[cancion]

	return res 

print(duracion(canciones, listas))