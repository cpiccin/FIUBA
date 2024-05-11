package comandos


import (
	"os"
	"fmt"
	"bufio"
	"strconv"
	"strings"
	v "tp2/vuelos"
	dicc "tdas/diccionario"
	heap "tdas/cola_prioridad"
	verifica "tp2/verificaciones"
)


func agregarArchivo(archivos []string, almacenaVuelos dicc.Diccionario[string, v.Vuelo], ordenaVuelos dicc.DiccionarioOrdenado[string, string]) {
	fileVuelos, err := os.Open(archivos[0])
	if ! verifica.VerificaArchivoValido(err) {
		return
	}
	procesarArchivo(fileVuelos, almacenaVuelos, ordenaVuelos)
	fileVuelos.Close()
}

func procesarArchivo(file *os.File, hashVuelos dicc.Diccionario[string, v.Vuelo], abbVuelosOrdenados dicc.DiccionarioOrdenado[string, string]) {
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		infoVuelo := strings.Split(strings.TrimSpace(scanner.Text()), ",")
		nuevoVuelo := v.CrearVuelo(infoVuelo)
		hashVuelos.Guardar(nuevoVuelo.Codigo(), nuevoVuelo)
	}
}

func prioridadVuelos(k int, almacenaVuelos dicc.Diccionario[string, v.Vuelo]) {
	arrAux := make([]v.Vuelo, almacenaVuelos.Cantidad())
	for iter, i := almacenaVuelos.Iterador(), 0; iter.HaySiguiente(); iter.Siguiente() {
		_, vuelo := iter.VerActual()
		arrAux[i] = vuelo
		i++
	}
	heapPrioridades := heap.CrearHeapArr[v.Vuelo](arrAux, funcCmpPrioridades)
	for i := 0; i < k; i++ {
		act := heapPrioridades.Desencolar()
		act.RepresentarVueloPrioridad()
	}
}

func funcCmpPrioridades(vuelo1, vuelo2 v.Vuelo) int {
	if vuelo1.Prioridad() >  vuelo2.Prioridad() {
		return 1
	}
	if vuelo1.Prioridad() == vuelo2.Prioridad() {
		return funcCmpCodigo(vuelo1.Codigo(), vuelo2.Codigo())
	}
	return -1
}

func funcCmpCodigo(codigo1, codigo2 string) int {
	if codigo1 < codigo2 {
		return 1
	}
	if codigo1 > codigo2 {
		return -1
	}
	return 0
}

func FuncCmpFechas(fecha1, fecha2 string) int {
	// supongo strings de la forma YYYYMMDDHHMMSS
	dia1, dia2 := strAInt(fecha1[:8]), strAInt(fecha2[:8])
	hora1, hora2 := strAInt(fecha1[8:]), strAInt(fecha2[8:])
	if dia1 > dia2 || (dia1 == dia2 && hora1 > hora2) {
		return -1
	}
	if dia1 < dia2 || (dia1 == dia2 && hora1 < hora2) {
		return 1
	}
	return 0
}

func strAInt(s string) int {
	sInt, _ := strconv.Atoi(s)
	return sInt
}