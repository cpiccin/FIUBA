package vuelos

import (
	"fmt"
	"os"
	"strconv"
	heap "tdas/cola_prioridad"
	l "tdas/lista"
)

// -- Vuelo -- //

type vuelo struct {
	flightNumber       string
	airline            string
	originAirport      string
	destinationAirport string
	tailNumber         string
	priority           int
	date               string
	departureDelay     int
	airTime            int
	cancelled          string
}

func CrearVuelo(info []string) Vuelo {
	prioridad, _ := strconv.Atoi(info[5])
	delay, _ := strconv.Atoi(info[7])
	airTime, _ := strconv.Atoi(info[8])
	return &vuelo{flightNumber: info[0],
		airline:            info[1],
		originAirport:      info[2],
		destinationAirport: info[3],
		tailNumber:         info[4],
		priority:           prioridad,
		date:               info[6],
		departureDelay:     delay,
		airTime:            airTime,
		cancelled:          info[9],
	}
}

func (vuelo *vuelo) Fecha() string {
	return vuelo.date
}

func (vuelo *vuelo) Codigo() string {
	return vuelo.flightNumber
}

func (vuelo *vuelo) Prioridad() int {
	return vuelo.priority
}

func (vuelo *vuelo) Origen() string {
	return vuelo.originAirport
}

func (vuelo *vuelo) Destino() string {
	return vuelo.destinationAirport
}

func (v *vuelo) RepresentarInformacion() {
	fmt.Fprintf(os.Stdout, "%s %s %s %s %s %d %s %d %d %s\n", v.flightNumber, v.airline, v.originAirport, v.destinationAirport, v.tailNumber, v.priority, v.date, v.departureDelay, v.airTime, v.cancelled)
}

func (v *vuelo) RepresentarVueloPrioridad() {
	fmt.Fprintf(os.Stdout, "%d - %s\n", v.priority, v.flightNumber)
}

func (v *vuelo) RepresentarVueloTablero() {
	fmt.Fprintf(os.Stdout, "%s - %s\n", v.date, v.flightNumber)
}

// -- VuelosEnFecha -- //

type vuelosEnFecha struct {
	vuelos l.Lista[Vuelo]
}

func CrearVuelosEnFecha() VuelosEnFecha {
	return &vuelosEnFecha{vuelos: l.CrearListaEnlazada[Vuelo]()}
}

func (v *vuelosEnFecha) AgregarVuelo(vuelo Vuelo) {
	lista := v.vuelos
	esta := false

	for iter := lista.Iterador(); iter.HaySiguiente(); iter.Siguiente() {
		if vuelo.Codigo() == iter.VerActual().Codigo() {
			esta = true
		}
	}

	if !esta {
		lista.InsertarUltimo(vuelo)
	}
}

func (v *vuelosEnFecha) BorrarVuelo(vuelo Vuelo) {
	lista := v.vuelos
	for iter := lista.Iterador(); iter.HaySiguiente(); iter.Siguiente() {
		if iter.VerActual().Codigo() == vuelo.Codigo() {
			iter.Borrar()
			break
		}
	}
}

func (v *vuelosEnFecha) ListaVuelos() l.Lista[Vuelo] {
	return v.vuelos
}

func (v *vuelosEnFecha) ColaVuelos(funcCmp func(Vuelo, Vuelo) int) heap.ColaPrioridad[Vuelo] {
	res := heap.CrearHeap[Vuelo](funcCmp)
	for iter := v.vuelos.Iterador(); iter.HaySiguiente(); iter.Siguiente() {
		res.Encolar(iter.VerActual())
	}
	return res
}
