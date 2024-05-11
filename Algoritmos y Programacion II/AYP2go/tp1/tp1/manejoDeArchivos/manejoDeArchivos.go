package archivos

import (
	"bufio"
	"os"
	"strconv"
	"strings"
	algoritmo "tp1/algoritmosAuxiliares"
	"tp1/errores"
	"tp1/votos"
)

func ProcesaArchivos(archivos []string) ([]votos.Partido, []votos.Votante, error) {
	var partidos []votos.Partido
	var padrones []votos.Votante
	if len(archivos) != 2 {
		return partidos, padrones, errores.ErrorParametros{}
	}
	fileLista, errL := os.Open(archivos[0])
	filePadron, errP := os.Open(archivos[1])
	if errL != nil || errP != nil {
		return partidos, padrones, errores.ErrorLeerArchivo{}
	}
	partidos = GenerarListaCandidaturas(fileLista)
	padrones = GenerarListaPadrones(filePadron)
	fileLista.Close()
	filePadron.Close()
	return partidos, padrones, nil
}

func GenerarListaCandidaturas(fileLista *os.File) []votos.Partido {
	var listas [][]string
	scannerL := bufio.NewScanner(fileLista)
	for scannerL.Scan() {
		lista := scannerL.Text()
		listas = append(listas, strings.Split(lista, ","))
	}
	var partidos []votos.Partido // lista de partidos [votosEnBlanco, lista1, lista2, ...]
	partidos = append(partidos, votos.CrearVotosEnBlanco())
	for i := 0; i < len(listas); i++ {
		arrAux := [3]string{}
		copy(arrAux[:], listas[i][1:])
		partidos = append(partidos, votos.CrearPartido(listas[i][0], arrAux))
	}
	return partidos
}

func GenerarListaPadrones(filePadron *os.File) []votos.Votante {
	scannerP := bufio.NewScanner(filePadron)
	var padrones []votos.Votante
	for scannerP.Scan() {
		padron := scannerP.Text()
		dni, _ := strconv.Atoi(padron)
		padrones = append(padrones, votos.CrearVotante(dni))
	}
	padrones = algoritmo.RadixSort(padrones)
	return padrones
}
