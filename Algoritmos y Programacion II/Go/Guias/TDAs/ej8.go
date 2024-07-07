package main 

import (
	"fmt"
	TDACola "TDAs/cola"
)

func main() {
	cola := TDACola.CrearColaEnlazada[int]()
	cola.Encolar(1)
	cola.Encolar(2)
	cola.Encolar(3)
	cola.Encolar(4)
	cola.Encolar(5)
	fmt.Println(Multiprimeros(cola, 45))
}


func Multiprimeros[T any](cola TDACola.Cola[T], k int) []T {
	cola_aux := TDACola.CrearColaEnlazada[T]()
	var slice_final []T
	for n := k; !cola.EstaVacia(); n-- {
		if n > 0 {
			slice_final = append(slice_final, cola.VerPrimero())
		}
		cola_aux.Encolar(cola.Desencolar())
	}
	for !cola_aux.EstaVacia() {
		cola.Encolar(cola_aux.Desencolar())
	}
	return slice_final
}