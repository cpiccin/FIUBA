package comandos

import (
	"fmt"
	"os"
	"strconv"
	"tdas/cola"
	"tp1/errores"
	verifica "tp1/verificaciones"
	"tp1/votos"
)

func Ingresar(args []string, padrones []votos.Votante, fila cola.Cola[votos.Votante], votanteActual *votos.Votante) {
	if len(args) != 1 {
		return
	}
	dniInt, err := strconv.Atoi(args[0])
	if !verifica.DNIValido(dniInt, err) {
		return
	}
	esta, pos := verifica.DNIEnPadron(dniInt, padrones)
	if !esta {
		return
	}
	fila.Encolar(padrones[pos])
	*votanteActual = fila.VerPrimero()
	fmt.Fprintf(os.Stdout, "OK\n")
}

func Votar(args []string, fila cola.Cola[votos.Votante], partidos []votos.Partido, votanteActual *votos.Votante) {
	if len(args) != 2 {
		return
	}
	tipoVoto := args[0]
	alternativa := args[1]
	if verifica.FilaVacia(fila) {
		return
	}
	if !verifica.TipoVotoValido(tipoVoto) {
		return
	}
	if !verifica.AlternativaValida(alternativa, len(partidos)-1) {
		return
	}
	alt, _ := strconv.Atoi(alternativa)
	var err error
	if tipoVoto == "Presidente" {
		err = (*votanteActual).Votar(votos.PRESIDENTE, alt)
	} else if tipoVoto == "Gobernador" {
		err = (*votanteActual).Votar(votos.GOBERNADOR, alt)
	} else if tipoVoto == "Intendente" {
		err = (*votanteActual).Votar(votos.INTENDENTE, alt)
	}
	if err != nil {
		fmt.Fprintf(os.Stdout, "%s\n", err.Error())
		fila.Desencolar()
		if !fila.EstaVacia() {
			*votanteActual = fila.VerPrimero()
		}
		return
	}
	fmt.Fprintf(os.Stdout, "OK\n")
}

func Deshacer(fila cola.Cola[votos.Votante], votanteActual *votos.Votante) {
	if verifica.FilaVacia(fila) {
		return
	}
	err := (*votanteActual).Deshacer()
	if err != nil {
		fmt.Fprintf(os.Stdout, "%s\n", err.Error())
		_, e := err.(errores.ErrorVotanteFraudulento)
		if e { // si se trata de un error de tipo votante fraudulento
			fila.Desencolar()
			if !fila.EstaVacia() {
				*votanteActual = fila.VerPrimero()
			}
		}
		return
	}
	fmt.Fprintf(os.Stdout, "OK\n")
}

func FinVotar(fila cola.Cola[votos.Votante], votanteActual *votos.Votante, urna votos.Urna) {
	if verifica.FilaVacia(fila) {
		return
	}

	voto, err := (*votanteActual).FinVoto()
	if err != nil {
		fmt.Fprintf(os.Stdout, "%s\n", err.Error())
		return
	}

	fila.Desencolar() // termina de votar y lo saco de la fila
	if !fila.EstaVacia() {
		*votanteActual = fila.VerPrimero() // si no esta vacia la fila el votante actual es el que sigue
	}

	urna.IngresarVoto(voto)
	fmt.Fprintf(os.Stdout, "OK\n")
}
