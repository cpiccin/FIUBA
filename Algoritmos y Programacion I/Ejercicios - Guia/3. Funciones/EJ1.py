# a) calcula la duracion en segundos de un intervalo dado en horas, minutos y segundos

def a_segundos(hora, minuto, segundo):
	segundos = segundo + minuto*60 + hora*3600
	return segundos

# b) Calcula cuantas horas, minutos y segundos son x cantidad de segundos

def a_horas_minutos(seg):
	minutos = seg//60
	seg_restantes = seg%60
	horas = minutos//60
	minutos_restantes = minutos%60
	return horas, minutos_restantes, seg_restantes



