from modelo_Cola import Cola, _Nodo

def promedio_espera(eventos):
	cola_pasajeros = Cola()
	suma = 0
	total = 0
	for event in eventos:
		if event[1] == 'c':
			for asiento in range(event[2]):
				if not cola_pasajeros.primero:
					break
				suma += event[0] - cola_pasajeros.primero.dato[0]
				total += 1
				cola_pasajeros.desencolar()
		else:
			cola_pasajeros.encolar(event)
	return suma/total

print(promedio_espera([(35,'p'), (43,'p'), (80,'c',1), (98,'p'), (142,'c',2)]))