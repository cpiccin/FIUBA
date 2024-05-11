import math, csv, funciones_grafo
from grafo import Grafo

PRECIO = 0
TIEMPO = 1
CANT_VUELOS = 2
FRECUENCIA = 3 


def procesa_archivos(entrada):

	aeropuertos_csv, vuelos_csv = entrada[1], entrada[2]
	grafo, ciudades, aeropuertos = Grafo(), {}, {}

	with open(aeropuertos_csv, "r") as a_csv, open(vuelos_csv, "r") as v_csv:
		
		reader_a, reader_v = csv.reader(a_csv), csv.reader(v_csv)

		for line in reader_a:
			
			codigo = line[1]
			grafo.agregar_vertice(codigo)
			aeropuertos[codigo] = line[2:]

			ciudad = line[0]
			ciudades[ciudad] = ciudades.get(ciudad, [])
			ciudades[ciudad].append(codigo)

		for line in reader_v:
			
			aero_i, aero_j, tiempo, precio, cant_vuelos = line[0], line[1], int(line[2]), int(line[3]), int(line[4])
			grafo.agregar_arista(aero_i, aero_j, [precio, tiempo, cant_vuelos, 1/cant_vuelos])

	return grafo, ciudades, aeropuertos


def procesa_input(entrada):
	e = entrada.split(" ", 1)

	comando = e[0]
	argumentos = e[1]

	if comando == "centralidad" or comando == "itinerario" or comando == "exportar_kml" or comando == "nueva_aerolinea":
		return comando, argumentos # es un solo comando, no hay separaciones con coma

	argumentos = argumentos.split(",")

	return comando, argumentos


def busca_mejor_ruta(origen, destino, grafo, ciudades, caminos_minimos, peso):

	ruta_minima = {}
	dist_minima = math.inf
	aeropuerto_origen, aeropuerto_destino = "", ""

	for a_o in ciudades[origen]:
		for a_d in ciudades[destino]:
			ruta, distancias = caminos_minimos(grafo, a_o, a_d, peso)
			if distancias[a_d] < dist_minima:
				dist_minima = distancias[a_d]
				ruta_minima = ruta 
				aeropuerto_origen, aeropuerto_destino = a_o, a_d 
	ruta = imprime_ruta(ruta_minima, aeropuerto_origen, aeropuerto_destino)
	return ruta 


def imprime_ruta(ruta, aeropuerto_origen, aeropuerto_destino):

	x = aeropuerto_destino
	res = []
	while x != aeropuerto_origen:
		res.append(x)
		x = ruta[x]
	res.append(x)

	for i in range(len(res)):
		a = res[len(res)-1-i]
		if a == aeropuerto_destino:
			print(a)
			break
		print(a, "-> ", end="")

	return res 


def define_ruta_segun_itinerario(archivo, ciudades, grafo):
	grafo_ciudades = crea_grafo_ciudades(archivo)
	ruta = funciones_grafo.orden_topologico_dfs(grafo_ciudades)

	cad = ""
	for i in range(len(ruta)):
		if i == len(ruta) -1 :
			cad += ruta[i]
			break
		cad += ruta[i] + ", "
	print(cad)

	for i in range(len(ruta)-1):
		busca_mejor_ruta(ruta[i], ruta[i+1], grafo, ciudades, funciones_grafo.caminos_minimos_bfs, None)


def crea_grafo_ciudades(archivo):
	grafo = Grafo(True)
	with open(archivo, "r") as ciudades_csv:
		reader_ciudades = csv.reader(ciudades_csv)
		ciudades = next(reader_ciudades)
		for ciudad in ciudades:
			grafo.agregar_vertice(ciudad)
		for linea in reader_ciudades:
			grafo.agregar_arista(linea[0], linea[1])
	return grafo


def imprime_centralidades(k, centralidades):
	cont = 0
	for a in centralidades:
		cont += 1
		if cont == k or cont == len(centralidades):
			print(a)
			break
		print(a, end=", ")


def algoritmo_centralidad(grafo, peso):
	cent  = {}
	for v in grafo.obtener_vertices():
		cent[v] = 0
	for v in grafo.obtener_vertices():
		padre, dist = funciones_grafo.caminos_minimos_dijkstra(grafo, v, None, peso)
		cent_aux = {}
		for w in grafo.obtener_vertices():
			cent_aux[w] = 0
		vertices_ordenados = ordenar_vertices(dist)
		for w in vertices_ordenados:
			if w not in padre or padre[w] is None:
				continue
			cent_aux[padre[w]] += 1 + cent_aux[w]
		for w in grafo.obtener_vertices():
			if w == v:
				continue
			cent[w] += cent_aux[w]
	cent = dict(sorted(cent.items(), key=lambda x: x[1], reverse=True))
	return cent 


def ordenar_vertices(dist):
	new_dic = {}
	for a in dist:
		if dist[a] != math.inf:
			new_dic[a] = dist[a]
	return dict(sorted(new_dic.items(), key=lambda x: x[1], reverse=True))


def escribe_archivo_csv(arbol, grafo, ruta):
	data = []
	for v,w,p in arbol.obtener_aristas():
		data.append([v, w, str(grafo.peso_arista(v, w)[TIEMPO]), str(p[PRECIO]), str(grafo.peso_arista(v, w))[CANT_VUELOS]])

	with open(ruta, "w", newline="") as file:
		writer = csv.writer(file)
		writer.writerows(data)


def generar_kml(archivo, ruta, aeropuertos):
	coordenadas = []
	for aero in ruta:
		coordenadas.append([aero] + aeropuertos[aero])
	coordenadas = coordenadas[::-1]
	with open(archivo, "w") as f:
		f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
		f.write('<kml xmlns="http://earth.google.com/kml/2.1">\n')
		f.write('	<Document>\n')
		for coord in coordenadas:
			code, lat, longt = coord[0], coord[1], coord[2]
			f.write('	<Placemark>\n')
			f.write(f'		<name>{code}</name>\n')
			f.write('		<Point>\n')
			f.write(f'			<coordinates>{longt}, {lat}</coordinates>\n')
			f.write('		</Point>\n')
			f.write('	</Placemark>\n')
			f.write('\n')
		for i in range(len(coordenadas)-1):
			lat1, long1, lat2, long2 = coordenadas[i][1], coordenadas[i][2], coordenadas[i+1][1], coordenadas[i+1][2]
			f.write('	<Placemark>\n')
			f.write('		<LineString>\n')
			f.write(f'			<coordinates>{long1}, {lat1} {long2}, {lat2}</coordinates>\n')
			f.write('		</LineString>\n')
			f.write('	</Placemark>\n')
			f.write('\n')
		f.write('	</Document>\n')
		f.write('</kml>\n')
