def signo_astrologico():
	dia = int(input('Ingrese su dia de nacimiento: '))
	mes = int(input('Ingrese su mes de nacimiento: '))
	if (mes == 3 and 21<=dia<=31) or (mes == 4 and 1<=dia<=20):
		return print('Su signo es Aries')
	if (mes == 5 and 21<=dia<=31) or (mes == 6 and 1<=dia<=21):
		return print('Su signo es Geminis')
	if (mes == 7 and 24<=dia<=31) or (mes == 8 and 1<=dia<=23):
		return print('Su sino es Leo')
	if (mes == 9 and 24<=dia<=30) or (mes == 10 and 1<=dia<=22):
		return print('Su signo es Libra')
	if (mes == 11 and 23<=dia<=30) or (mes == 12 and 1<=dia<=21):
		return print('Su signo es Sagitario')
	if (mes == 1 and 21<=dia<=31) or (mes == 2 and 1<=dia<=19):
		return print('Su signo es Acuario')
	if (mes == 4 and 21<=dia<=30) or (mes == 5 and 1<=dia<=20):
		return print('Su signo es Tauro')
	if (mes == 6 and 22<=dia<=30) or (mes == 7 and 1<=dia<=23):
		return print('Su signo es Cancer')
	if (mes == 8 and 24<=dia<=31) or (mes == 9 and 1<=dia<=23):
		return print('Su signo es Virgo')
	if (mes == 10 and 23<=dia<=31) or (mes == 11 and 1<=dia<=22):
		return print('Su signo es Escorpio')
	if (mes == 12 and 22<=dia<=31) or (mes == 1 and 1<=dia<=20):
		return print('Su signo es Capricornio')
	if (mes == 2 and 20<=dia<=29) or (mes == 3 and 1<=dia<=20):
		return print('Su signo es Piscis')

signo_astrologico()