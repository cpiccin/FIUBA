package comandos

import (
	"fmt"
	"os"
	dicc "tdas/diccionario"
	verifica "tp2/verificaciones"
	v "tp2/vuelos"
)

func AgregarArchivo(archivos []string, almacenadorDeVuelos dicc.Diccionario[string, v.Vuelo], ordenaVuelosAsc dicc.DiccionarioOrdenado[int, v.VuelosEnFecha], ordenaVuelosDesc dicc.DiccionarioOrdenado[int, v.VuelosEnFecha]) {
	if !verifica.VerificaInputAgregarArchivo(archivos) {
		return
	}
	if !agregarArchivo(archivos, almacenadorDeVuelos, ordenaVuelosAsc, ordenaVuelosDesc) {
		return
	}
	fmt.Fprintf(os.Stdout, "OK\n")
}

func VerTablero(args []string, ordenaVuelosAsc dicc.DiccionarioOrdenado[int, v.VuelosEnFecha], ordenaVuelosDesc dicc.DiccionarioOrdenado[int, v.VuelosEnFecha]) {
	verificacion, k, modo, desde, hasta := verifica.VerificaInputVerTablero(args)
	if !verificacion {
		return
	}
	if modo == "desc" {
		verTablero(k, desde, hasta, modo, ordenaVuelosDesc)
	} else {
		verTablero(k, desde, hasta, modo, ordenaVuelosAsc)
	}

	fmt.Fprintf(os.Stdout, "OK\n")
}

func InfoVuelo(codigo []string, almacenadorDeVuelos dicc.Diccionario[string, v.Vuelo]) {
	if !verifica.VerificaInputInfoVuelo(codigo) {
		return
	}
	if !verifica.VerificaCodigoExistente(codigo, almacenadorDeVuelos) {
		return
	}
	infoVuelo(codigo[0], almacenadorDeVuelos)
	fmt.Fprintf(os.Stdout, "OK\n")
}

func PrioridadVuelos(args []string, almacenadorDeVuelos dicc.Diccionario[string, v.Vuelo]) {
	verificacion, k := verifica.VerificaInputPrioridadVuelos(args)
	if !verificacion {
		return
	}
	prioridadVuelos(k, almacenadorDeVuelos)
	fmt.Fprintf(os.Stdout, "OK\n")
}

func SiguienteVuelo(args []string, ordenaVuelos dicc.DiccionarioOrdenado[int, v.VuelosEnFecha]) {
	verificacion, origen, destino, fecha := verifica.VerificaInputSiguienteVuelo(args)
	if !verificacion {
		return
	}
	siguienteVuelo(origen, destino, fecha, ordenaVuelos)
	fmt.Fprintf(os.Stdout, "OK\n")
}

func Borrar(args []string, almacenadorDeVuelos dicc.Diccionario[string, v.Vuelo], ordenaVuelosAsc dicc.DiccionarioOrdenado[int, v.VuelosEnFecha], ordenaVuelosDesc dicc.DiccionarioOrdenado[int, v.VuelosEnFecha]) {
	verificacion, desde, hasta := verifica.VerificaInputBorrar(args)
	if !verificacion {
		return
	}
	borrar(desde, hasta, almacenadorDeVuelos, ordenaVuelosAsc, ordenaVuelosDesc)
	fmt.Fprintf(os.Stdout, "OK\n")
}
