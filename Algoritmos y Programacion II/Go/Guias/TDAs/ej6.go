// Dada una pila de enteros, escribir una función que determine si sus elementos están ordenados de manera ascendente. 
// Una pila de enteros está ordenada de manera ascendente si, en el sentido que va desde el tope de la pila hacia el 
// resto de elementos, cada elemento es menor al elemento que le sigue. La pila debe quedar en el mismo estado que al 
// invocarse la función. 
// Indicar y justificar el orden del algoritmo propuesto.

package main

import (
	"fmt"
	tda "tdas/pila"
)

func main() {

}

func OrdenadosAscendentes(pila tda.Pila[int]) bool {
	pilaAux := tda.CrearPilaDinamica[int]()
	anterior := pila.Desapilar() // tope
	pilaAux.Apilar(anterior)
	esAsc := false

	for ! pila.EstaVacia() {
		elem := pila.Desapilar()
		pilaAux.Apilar(elem)
		if elem <= anterior {
			esAsc = true
		}
		anterior = elem
	}

	for ! pilaAux.EstaVacia() {
		// para reestablecer la pila
		pila.Apilar(pilaAux.Desapilar())
	}

	if esAsc {
		return false
	}
	return true
} 