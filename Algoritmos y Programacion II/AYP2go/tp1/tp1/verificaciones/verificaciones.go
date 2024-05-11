package verificaciones

import (
	"fmt"
	"os"
	"strconv"
	"tdas/cola"
	algoritmo "tp1/algoritmosAuxiliares"
	"tp1/errores"
	"tp1/votos"
)

func DNIEnPadron(dni int, padrones []votos.Votante) (bool, int) {
	//busco por busqueda binaria el DNI
	pos := algoritmo.BusquedaBinaria(padrones, dni, 0, len(padrones)-1)
	if pos == -1 {
		fmt.Fprintf(os.Stdout, "%s\n", errores.DNIFueraPadron{}.Error())
		return false, pos
	}
	return true, pos
}

func DNIValido(dni int, err error) bool {
	if err != nil || dni < 0 {
		fmt.Fprintf(os.Stdout, "%s\n", errores.DNIError{}.Error())
		return false // el DNI es invalido
	}
	return true
}

func AlternativaValida(alt string, cant_listas int) bool {
	alt_int, err := strconv.Atoi(alt)
	if err != nil || (alt_int < 0 || alt_int > cant_listas) {
		fmt.Fprintf(os.Stdout, "%s\n", errores.ErrorAlternativaInvalida{}.Error())
		return false
	}
	return true
}

func TipoVotoValido(tipo string) bool {
	if tipo != "Presidente" && tipo != "Gobernador" && tipo != "Intendente" { // verifica que se ingrese un cargo valido
		fmt.Fprintf(os.Stdout, "%s\n", errores.ErrorTipoVoto{}.Error())
		return false
	}
	return true
}

func FilaVacia(fila cola.Cola[votos.Votante]) bool {
	if fila.EstaVacia() {
		fmt.Fprintf(os.Stdout, "%s\n", errores.FilaVacia{}.Error())
		return true
	}
	return false
}
