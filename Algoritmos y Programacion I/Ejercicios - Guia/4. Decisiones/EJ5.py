# a) Dado un anio indica si es bisiesto
# Un anio es bisiesto si es divisible por 4, no es divisible por 100
# excepto que tmb es divisible por 400


def es_bisiesto(n):
	if n%4 == 0 and n%100 != 0:
		return True
	if n%4 == 0 and n%100 != 0 and n%400 == 0:
		return True
	return False


# b) Dado un mes y un anio devuelve la cantidad de dias correspondientes

def cantidad_de_dias(mes, año): # pensando que el mes esta en numero
	if mes == 0:
		return '0 no corresponde a un mes valido.'
	cantidad_de_dias = 0
	if es_bisiesto(año) == True:
		if mes == 2:
			cantidad_de_dias += 29
			return cantidad_de_dias
	else:
		if mes == 2:
			cantidad_de_dias += 28
			return cantidad_de_dias
	if mes in (1, 3, 5, 7, 8, 10, 12):
		cantidad_de_dias += 31
		return cantidad_de_dias
	if mes in (4, 6, 9, 11):
		cantidad_de_dias += 30
		return cantidad_de_dias


# c) Dada una fecha indica si es valida o no.

def fecha_valida(dia, mes, año):
	if not 1<=dia<=31 or not 1<=mes<=12 or not 0<=año:
		return False
	if es_bisiesto(año) == False:
		if 1<=dia<=31 and mes in (1, 3, 5, 7, 8, 10, 12):
			return True
		if 1<=dia<=30 and mes in (4, 6, 9, 11):
			return True
		if 1<=dia<=28 and mes == 2:
			return True
		return False
	if es_bisiesto(año) == True:
		if 1<=dia<=31 and mes in (1, 3, 5, 7, 8, 10, 12):
			return True
		if 1<=dia<=30 and mes in (4, 6, 9, 11):
			return True
		if 1<=dia<=29 and mes == 2:
			return True
		return False


# d) Dada una fecha indica cuantos dias faltan para fin de mes
def fin_de_mes(dia, mes, año):
	return cantidad_de_dias(mes, año) - dia 

# e) Dada un fecha indica cuantos dias faltan para fin de año
def fin_de_año(dia, mes, año):
	hasta_fin_de_año = 0
	if fecha_valida(dia, mes, año) == True:
		for i in range(mes, 13):
			hasta_fin_de_año += cantidad_de_dias(i, año)
		return hasta_fin_de_año - dia 
	return False


# f) Dada una fecha indica cuantos dias transcurrieron en ese año hasta la fecha
def dias_transcurridos(dia, mes, año):
	dias_transcurridos = 0
	if fecha_valida(dia, mes, año) == True:
		for i in range(1, mes):
			dias_transcurridos += cantidad_de_dias(i, año)
		return dias_transcurridos + dia
	return False



