from EJ1 import *

def monto_final_pregunta():
	pesos = int(input('Ingrese cantidad de pesos: '))
	tasa = int(input('Ingrese tasa de interes: '))
	años = int(input('Ingrese cantidad de años: '))
	monto = monto_final(pesos, tasa, años)
	return print(monto)

