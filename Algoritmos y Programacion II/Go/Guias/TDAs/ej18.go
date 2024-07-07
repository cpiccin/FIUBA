// Implementar una función recursiva que reciba una pila y devuelva la cantidad de elementos de la misma. 
// Al terminar la ejecución de la función la pila debe quedar en el mismo estado al original.

package main

import (
	"fmt"
	tda "tdas/pila"
)


func main() {
	pila := tda.CrearPilaDinamica[int]()
	pila.Apilar(3)
	pila.Apilar(8)
	pila.Apilar(9)
	pila.Apilar(2)
	pila.Apilar(19)
	fmt.Println(pila.Representar())
	fmt.Println(Largo(pila))
}

func Largo[T any](pila tda.Pila[T]) int {
	return largoRec(pila, 0)
}

func largoRec[T any](pila tda.Pila[T], cont int) int {
	if pila.EstaVacia() {
		return cont
	}
	elem := pila.Desapilar()
	contador := largoRec(pila, cont+1)
	pila.Apilar(elem)
	return contador
}