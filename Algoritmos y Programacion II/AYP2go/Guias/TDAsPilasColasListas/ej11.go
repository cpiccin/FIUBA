// Implementar una función que ordene de manera ascendente una pila de enteros sin conocer su estructura interna 
// y utilizando como estructura auxiliar sólo otra pila auxiliar. Por ejemplo, la pila [ 4, 1, 5, 2, 3 ] debe quedar
// como [ 1, 2, 3, 4, 5 ] (siendo el último elemento el tope de la pila, en ambos casos). 
// Indicar y justificar el orden de la función.

package main 

import (
	"fmt"
	tda "tdas/pila"
)

func main() {

}



func Ordenar(pila Pila[int]) {
	pilaAux := CrearPilaDinamica[int]()
	for ! pila.EstaVacia() {
		elem := pila.Desapilar()
		for ! pilaAux.EstaVacia() && elem > pilaAux.VerTope() {
			pila.Apilar(pilaAux.Desapilar())
		}
		pilaAux.Apilar(elem)
	}
	for ! pilaAux.EstaVacia() {
		pila.Apilar(pilaAux.Desapilar())
	}
}
