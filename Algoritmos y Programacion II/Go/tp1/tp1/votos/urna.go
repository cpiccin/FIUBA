package votos

type Urna interface {
	//Muestra por pantalla los resultados finales
	ImprimirResultados(partidos []Partido)
	//Ingresa un voto a la urna para su posterior conteo
	IngresarVoto(voto Voto)
	//Distribuye los votos finales a cada partido
	ConteoFinal(partido []Partido)
}
