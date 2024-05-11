package verificaciones

import (
	"fmt"
	"os"
	"strconv"
	dicc "tdas/diccionario"
	aux "tp2/auxiliares"
	v "tp2/vuelos"
)

func VerificaInputAgregarArchivo(archivos []string) bool {
	if len(archivos) != 1 {
		fmt.Fprintf(os.Stderr, "%s\n", ErrorComando{}.Error("agregar_archivo"))
		return false
	}
	return true
}

func VerificaArchivoValido(err error) bool {
	if err != nil {
		fmt.Fprintf(os.Stderr, "%s\n", ErrorComando{}.Error("agregar_archivo"))
		return false
	}
	return true
}

func VerificaInputInfoVuelo(param []string) bool {
	if len(param) != 1 {
		fmt.Fprintf(os.Stderr, "%s\n", ErrorComando{}.Error("info_vuelo"))
		return false
	}
	_, err := strconv.Atoi(param[0]) // veo que tenga solo numeros
	if err != nil {
		fmt.Fprintf(os.Stderr, "%s\n", ErrorComando{}.Error("info_vuelo"))
		return false
	}
	return true
}

func VerificaCodigoExistente(codigo []string, vuelos dicc.Diccionario[string, v.Vuelo]) bool {
	if !vuelos.Pertenece(codigo[0]) {
		fmt.Fprintf(os.Stderr, "%s\n", ErrorComando{}.Error("info_vuelo"))
		return false
	}
	return true
}

func VerificaInputPrioridadVuelos(k []string) (bool, int) {
	if len(k) != 1 {
		fmt.Fprintf(os.Stderr, "%s\n", ErrorComando{}.Error("prioridad_vuelos"))
		return false, 0
	}
	kInt, err := strconv.Atoi(k[0])
	if err != nil || kInt <= 0 {
		fmt.Fprintf(os.Stderr, "%s\n", ErrorComando{}.Error("prioridad_vuelos"))
		return false, 0
	}
	return true, kInt
}

func VerificaInputVerTablero(args []string) (bool, int, string, int, int) {
	if len(args) != 4 {
		fmt.Fprintf(os.Stderr, "%s\n", ErrorComando{}.Error("ver_tablero"))
		return false, 0, "", 0, 0
	}
	kInt, errK := strconv.Atoi(args[0])
	modo := args[1]
	desdeInt, errDesde := aux.FechaAInt(args[2])
	hastaInt, errHasta := aux.FechaAInt(args[3])
	if (errK != nil || kInt <= 0) || (modo != "asc" && modo != "desc") || (errHasta != nil || errDesde != nil) {
		fmt.Fprintf(os.Stderr, "%s\n", ErrorComando{}.Error("ver_tablero"))
		return false, 0, "", 0, 0
	}
	return true, kInt, modo, desdeInt, hastaInt
}

func VerificaInputSiguienteVuelo(args []string) (bool, string, string, string) {
	if len(args) != 3 {
		fmt.Fprintf(os.Stderr, "%s\n", ErrorComando{}.Error("siguiente_vuelo"))
		return false, "", "", ""
	}
	_, errFecha := aux.FechaAInt(args[2])
	if errFecha != nil {
		fmt.Fprintf(os.Stderr, "%s\n", ErrorComando{}.Error("siguiente_vuelo"))
		return false, "", "", ""
	}
	return true, args[0], args[1], args[2] // me interesa devolver la fecha como string
}

func VerificaInputBorrar(args []string) (bool, int, int) {
	if len(args) != 2 {
		fmt.Fprintf(os.Stderr, "%s\n", ErrorComando{}.Error("borrar"))
		return false, 0, 0
	}
	desdeInt, errDesde := aux.FechaAInt(args[0])
	hastaInt, errHasta := aux.FechaAInt(args[1])
	if desdeInt > hastaInt || errDesde != nil || errHasta != nil {
		fmt.Fprintf(os.Stdout, "OK\n")
		return false, 0, 0
	}
	return true, desdeInt, hastaInt
}
