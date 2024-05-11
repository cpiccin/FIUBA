import csv

def lugares(ruta, persona):
	contacto = []
	donde_estuvo = []
	lugares = {}
	with open(ruta) as archivo:
		for nombre, lugar, donde in csv.reader(archivo, delimiter=';'):
			if nombre==persona:
				donde_estuvo.append((lugar, donde))
			else:
				lugares[nombre] = (lugar, donde)
	for nombre, lugar in lugares.items():
		if lugar in donde_estuvo:
			contacto.append(nombre)

	return contacto




print(lugares('personas.csv', 'Candela'))




