import auxiliares, funciones_grafo, csv


def camino_mas(argumentos, grafo, ciudades):
	modo, origen, destino = argumentos[0], argumentos[1], argumentos[2]

	if modo == "barato":
		return auxiliares.busca_mejor_ruta(origen, destino, grafo, ciudades, funciones_grafo.caminos_minimos_dijkstra, auxiliares.PRECIO)
	return auxiliares.busca_mejor_ruta(origen, destino, grafo, ciudades, funciones_grafo.caminos_minimos_dijkstra, auxiliares.TIEMPO)


def camino_escalas(argumentos, grafo, ciudades):
	origen, destino = argumentos[0], argumentos[1]
	return auxiliares.busca_mejor_ruta(origen, destino, grafo, ciudades, funciones_grafo.caminos_minimos_bfs, None)


def centralidad(argumentos, grafo):
	centralidades = auxiliares.algoritmo_centralidad(grafo, auxiliares.FRECUENCIA)
	auxiliares.imprime_centralidades(int(argumentos), centralidades)


def nueva_aerolinea(argumentos, grafo):
	mst = funciones_grafo.mst_prim(grafo, auxiliares.PRECIO)
	auxiliares.escribe_archivo_csv(mst, grafo, argumentos)
	print("OK")


def itinerario(argumentos, ciudades, grafo):
	auxiliares.define_ruta_segun_itinerario(argumentos, ciudades, grafo)


def exportar_kml(argumentos, ruta, aeropuertos):
	auxiliares.generar_kml(argumentos, ruta, aeropuertos)
	print("OK")
	