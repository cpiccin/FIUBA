package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
	"tdas/cola"
	"tp1/comandos"
	"tp1/errores"
	file "tp1/manejoDeArchivos"
	"tp1/votos"
)

func main() {

	archivos := os.Args[1:]

	partidos, padrones, err := file.ProcesaArchivos(archivos)

	if err != nil {
		fmt.Fprintf(os.Stdout, "%s\n", err)
		return
	}

	var votanteActual votos.Votante
	urna := votos.CrearUrna()

	scanner := bufio.NewScanner(os.Stdin)
	fila := cola.CrearColaEnlazada[votos.Votante]() // fila de votantes esperando para votar

	for scanner.Scan() { // loop, se sale del ciclo cuando se cierra stdin

		input := strings.Split(strings.TrimSpace(scanner.Text()), " ")
		comando := input[0]
		args := input[1:]

		switch comando {

		case "ingresar":

			comandos.Ingresar(args, padrones, fila, &votanteActual)

		case "votar":

			comandos.Votar(args, fila, partidos, &votanteActual)

		case "deshacer":

			comandos.Deshacer(fila, &votanteActual)

		case "fin-votar":

			comandos.FinVotar(fila, &votanteActual, urna)

		}
	}

	if !fila.EstaVacia() {
		fmt.Fprintf(os.Stdout, "%s\n", errores.ErrorCiudadanosSinVotar{}.Error())
	}

	urna.ConteoFinal(partidos)
	urna.ImprimirResultados(partidos)
}
