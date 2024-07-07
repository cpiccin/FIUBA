// Implementar en lenguaje Go una función recursiva con la firma func esHeap(arr []int). Esta función debe devolver true o false de acuerdo a si el 
// arreglo que recibe como parámetro cumple la propiedad de heap (de mínimos).

package main 

import (
	"fmt"
)

func esHeap(arr []int) bool {
    return aux(arr, 0)
}

func aux(arr []int, pos int) bool {
	n := len(arr)
	h_izq := 2*pos + 1
	h_der := 2*pos + 2

	if (h_izq < n && arr[pos] > arr[h_izq]) || (h_der < n && arr[pos] > arr[h_der]) {
		return false
	}

	if (h_izq < n && !aux(arr, h_izq)) || (h_der < n && !aux(arr, h_der)) {
        //si es un hijo pero ese hijo no pasa el if de arriba, chau
		return false
	}

	return true
}

