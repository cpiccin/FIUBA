package main

import (
	"bufio"
	"os"
	"strings"
	dicc "tdas/diccionario"
	aux "tp2/auxiliares"
	comandos "tp2/comandos"
	v "tp2/vuelos"
)

func main() {

	almacenadorDeVuelos := dicc.CrearHash[string, v.Vuelo]()
	ordenaVuelosAsc := dicc.CrearABB[int, v.VuelosEnFecha](aux.FuncCmpAbbFechaAsc)
	ordenaVuelosDesc := dicc.CrearABB[int, v.VuelosEnFecha](aux.FuncCmpAbbFechaDesc)

	scanner := bufio.NewScanner(os.Stdin)

	for scanner.Scan() {
		input := strings.Split(strings.TrimSpace(scanner.Text()), " ")
		comando := input[0]
		args := input[1:]

		switch comando {

		case "agregar_archivo":
			comandos.AgregarArchivo(args, almacenadorDeVuelos, ordenaVuelosAsc, ordenaVuelosDesc)
		case "ver_tablero":
			comandos.VerTablero(args, ordenaVuelosAsc, ordenaVuelosDesc)
		case "info_vuelo":
			comandos.InfoVuelo(args, almacenadorDeVuelos)
		case "prioridad_vuelos":
			comandos.PrioridadVuelos(args, almacenadorDeVuelos)
		case "siguiente_vuelo":
			comandos.SiguienteVuelo(args, ordenaVuelosAsc)
		case "borrar":
			comandos.Borrar(args, almacenadorDeVuelos, ordenaVuelosAsc, ordenaVuelosDesc)
		}
	}
}
