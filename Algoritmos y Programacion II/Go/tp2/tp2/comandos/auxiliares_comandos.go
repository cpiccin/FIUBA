package comandos

import (
	"bufio"
	"fmt"
	"os"
	"strings"
	heap "tdas/cola_prioridad"
	dicc "tdas/diccionario"
	aux "tp2/auxiliares"
	verifica "tp2/verificaciones"
	v "tp2/vuelos"
)

func agregarArchivo(archivos []string, almacenadorDeVuelos dicc.Diccionario[string, v.Vuelo], ordenaVuelosAsc dicc.DiccionarioOrdenado[int, v.VuelosEnFecha], ordenaVuelosDesc dicc.DiccionarioOrdenado[int, v.VuelosEnFecha]) bool {
	fileVuelos, err := os.Open(archivos[0])
	if !verifica.VerificaArchivoValido(err) {
		return false
	}
	procesarArchivo(fileVuelos, almacenadorDeVuelos, ordenaVuelosAsc, ordenaVuelosDesc)
	fileVuelos.Close()
	return true
}

func procesarArchivo(file *os.File, almacenadorDeVuelos dicc.Diccionario[string, v.Vuelo], ordenaVuelosAsc dicc.DiccionarioOrdenado[int, v.VuelosEnFecha], ordenaVuelosDesc dicc.DiccionarioOrdenado[int, v.VuelosEnFecha]) {
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		infoVuelo := strings.Split(strings.TrimSpace(scanner.Text()), ",")
		nuevoVuelo := v.CrearVuelo(infoVuelo)
		actualizarVuelosOrdenados(nuevoVuelo, ordenaVuelosDesc, almacenadorDeVuelos)
		actualizarVuelosOrdenados(nuevoVuelo, ordenaVuelosAsc, almacenadorDeVuelos)
		almacenadorDeVuelos.Guardar(nuevoVuelo.Codigo(), nuevoVuelo)
	}
}

func actualizarVuelosOrdenados(nuevoVuelo v.Vuelo, ordenaVuelos dicc.DiccionarioOrdenado[int, v.VuelosEnFecha], almacenadorDeVuelos dicc.Diccionario[string, v.Vuelo]) {
	code := nuevoVuelo.Codigo()
	nuevaFecha, _ := aux.FechaAInt(nuevoVuelo.Fecha())

	if almacenadorDeVuelos.Pertenece(code) { // el codigo ya fue ingresado alguna vez
		vueloPrevio := almacenadorDeVuelos.Obtener(code)
		fechaPrevia, _ := aux.FechaAInt(vueloPrevio.Fecha())
		if fechaPrevia != nuevaFecha { // el vuelo cambio de fecha, lo borro de la fecha previa
			listaFechaPrevia := ordenaVuelos.Obtener(fechaPrevia)
			listaFechaPrevia.BorrarVuelo(nuevoVuelo)
			ordenaVuelos.Guardar(fechaPrevia, listaFechaPrevia)
		} else if fechaPrevia == nuevaFecha && vueloPrevio != nuevoVuelo {
			listaVuelos := ordenaVuelos.Obtener(nuevaFecha)
			listaVuelos.BorrarVuelo(vueloPrevio)
			listaVuelos.AgregarVuelo(nuevoVuelo)
			ordenaVuelos.Guardar(nuevaFecha, listaVuelos)
			return
		}
	}

	if ordenaVuelos.Pertenece(nuevaFecha) { // si la nuevaFecha ya existe en el abb tengo que modificar su lista
		listaDeVuelos := ordenaVuelos.Obtener(nuevaFecha)
		listaDeVuelos.AgregarVuelo(nuevoVuelo)
		ordenaVuelos.Guardar(nuevaFecha, listaDeVuelos)
	} else { // si no existe creo una nueva clave-valor con fecha-lista
		nuevaListaDeVuelos := v.CrearVuelosEnFecha()
		nuevaListaDeVuelos.AgregarVuelo(nuevoVuelo)
		ordenaVuelos.Guardar(nuevaFecha, nuevaListaDeVuelos)
	}
}

func verTablero(k, desde, hasta int, modo string, ordenaVuelos dicc.DiccionarioOrdenado[int, v.VuelosEnFecha]) {
	funcCmp := aux.FuncCmpHeapFechaAsc

	if modo == "desc" {
		funcCmp = aux.FuncCmpHeapFechaDesc
		desde, hasta = hasta, desde
	}

	for iter, i := ordenaVuelos.IteradorRango(&desde, &hasta), 0; iter.HaySiguiente(); iter.Siguiente() {
		// itero sobre cada fecha del arbol
		_, vuelos := iter.VerActual()
		// itero sobre cada vuelo en la fecha
		vuelosCola := vuelos.ColaVuelos(funcCmp)
		for !vuelosCola.EstaVacia() && i < k {
			vuelosCola.Desencolar().RepresentarVueloTablero()
			i++
		}
	}
}

func infoVuelo(codigo string, almacenadorDeVuelos dicc.Diccionario[string, v.Vuelo]) {
	vueloPedido := almacenadorDeVuelos.Obtener(codigo)
	vueloPedido.RepresentarInformacion()
}

func prioridadVuelos(k int, almacenadorDeVuelos dicc.Diccionario[string, v.Vuelo]) {
	arrAux := make([]v.Vuelo, almacenadorDeVuelos.Cantidad())
	for iter, i := almacenadorDeVuelos.Iterador(), 0; iter.HaySiguiente(); iter.Siguiente() {
		_, vuelo := iter.VerActual()
		arrAux[i] = vuelo
		i++
	}
	heapPrioridades := heap.CrearHeapArr[v.Vuelo](arrAux, aux.FuncCmpHeapPrioridades)
	for i := 0; !heapPrioridades.EstaVacia() && i < k; i++ {
		act := heapPrioridades.Desencolar()
		act.RepresentarVueloPrioridad()
	}
}

func siguienteVuelo(origen, destino, fecha string, ordenaVuelos dicc.DiccionarioOrdenado[int, v.VuelosEnFecha]) {
	hayVuelo := false
	fechaInt, _ := aux.FechaAInt(fecha)

	for iter := ordenaVuelos.IteradorRango(&fechaInt, nil); !hayVuelo && iter.HaySiguiente(); iter.Siguiente() {
		_, vuelos := iter.VerActual()
		vuelosCola := vuelos.ColaVuelos(aux.FuncCmpHeapFechaAsc)
		for !vuelosCola.EstaVacia() {
			act := vuelosCola.Desencolar()
			if act.Origen() == origen && act.Destino() == destino {
				act.RepresentarInformacion()
				hayVuelo = true
			}
		}
	}
	if !hayVuelo {
		fmt.Fprintf(os.Stdout, "No hay vuelo registrado desde %s hacia %s desde %s\n", origen, destino, fecha)
	}
}

func borrar(desde, hasta int, almacenadorDeVuelos dicc.Diccionario[string, v.Vuelo], ordenaVuelosAsc dicc.DiccionarioOrdenado[int, v.VuelosEnFecha], ordenaVuelosDesc dicc.DiccionarioOrdenado[int, v.VuelosEnFecha]) {
	for iter := ordenaVuelosAsc.IteradorRango(&desde, &hasta); iter.HaySiguiente(); {
		fecha, vuelos := iter.VerActual()
		vuelosCola := vuelos.ColaVuelos(aux.FuncCmpHeapFechaAsc)
		for !vuelosCola.EstaVacia() {
			act := vuelosCola.Desencolar()
			almacenadorDeVuelos.Borrar(act.Codigo())
			act.RepresentarInformacion()
		}
		ordenaVuelosAsc.Borrar(fecha)
		ordenaVuelosDesc.Borrar(fecha)
		iter.Siguiente()
	}
}
