#!/usr/bin/python3
import sys, auxiliares, comandos
from grafo import Grafo 


def main():

	entrada = sys.argv
	grafo, ciudades, aeropuertos = auxiliares.procesa_archivos(entrada)
	ultima_ruta = ""

	while True:

		try:
			entrada_usuario = input()
			comando, argumentos = auxiliares.procesa_input(entrada_usuario)

			if comando == "camino_mas":
				ultima_ruta = comandos.camino_mas(argumentos, grafo, ciudades)
			elif comando == "camino_escalas":
				ultima_ruta = comandos.camino_escalas(argumentos, grafo, ciudades)
			elif comando == "centralidad":
				comandos.centralidad(argumentos, grafo)
			elif comando == "nueva_aerolinea":
				comandos.nueva_aerolinea(argumentos, grafo)
			elif comando == "itinerario":
				comandos.itinerario(argumentos, ciudades, grafo)
			elif comando == "exportar_kml":
				comandos.exportar_kml(argumentos, ultima_ruta, aeropuertos)
			else:
				continue

		except EOFError:
			break


main()