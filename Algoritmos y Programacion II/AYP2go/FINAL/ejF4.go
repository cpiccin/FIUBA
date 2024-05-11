// Implementar un algoritmo que reciba un arreglo desordenado de enteros, su largo (n) y un número K y determinar en
// O(n) si existe un par de elementos en el arreglo que sumen exactamente K

package main

import (
	"fmt"
	tda "tdas/diccionario"
)


func parSumaK(arr []int, k int) bool {
	aux := tda.CrearHash[int, int]()
	for _, n := range arr {
		comp := k - n 
		if aux.Pertenece(n) {
			return true 
		}
		aux.Guardar(comp, n)
	}
	return false
}

func main() {
	arr := []int{5, 4, 7, 1, 2, -3}
	k := 13 // false 
	fmt.Println(parSumaK(arr, k))
}