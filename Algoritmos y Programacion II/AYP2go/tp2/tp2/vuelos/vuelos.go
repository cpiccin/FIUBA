package vuelos

import (
	heap "tdas/cola_prioridad"
	l "tdas/lista"
)

type Vuelo interface {
	// Devuelve una cadena con la fecha del vuelo
	Fecha() string
	// Devuelve una cadena con el codigo del vuelo
	Codigo() string
	// Devuelve un entero que es la prioridad del vuelo
	Prioridad() int
	// Devuelve el aeropuerto de origen
	Origen() string
	// Devuelve el aeropuerto de destino
	Destino() string
	// Muestra en pantalla toda la informacion del vuelo
	RepresentarInformacion()
	// Muestra en pantalla la prioridad y el codigo del vuelo
	RepresentarVueloPrioridad()
	// Muestra en pantalla la fecha y codigo del vuelo
	RepresentarVueloTablero()
}

type VuelosEnFecha interface {
	// Agrega un vuelo a la fecha
	AgregarVuelo(vuelo Vuelo)
	// Borra un vuelo de la fecha
	BorrarVuelo(vuelo Vuelo)
	// Devuelve una lista enlazada que almacena los vuelos actuales en la fecha
	ListaVuelos() l.Lista[Vuelo]
	// Devuelve una cola de prioridad que desencola segun la funcion de comparacion recibida
	ColaVuelos(funcCmp func(Vuelo, Vuelo) int) heap.ColaPrioridad[Vuelo]
}
