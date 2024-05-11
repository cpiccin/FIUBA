// Se tiene un arreglo tal que [1, 1, 1, ..., 0, 0, ...] (es decir, unos seguidos de ceros). 
// Se pide: una función de orden O(log n) que encuentre el índice del primer 0. Si no hay ningún 0 
// (solo hay unos), debe devolver -1.
// Demostrar con el Teorema Maestro que la función es, en efecto, O(log n) 


package main

import "fmt"


func main() {
	arr := []int{1,1,1,1,1}
	fmt.Println(primerCero(arr))
}

func primerCero(arr []int) int {
	return aux(arr, 0, len(arr)-1)
}

func aux(arr []int, ini, fin int) int {
	if ini == fin {
		if arr[ini] == 0 {
			return ini
		} else {
			return -1
		}
	}
	medio := (ini+fin)/2
	if arr[medio] == 1 {
		return aux(arr, medio+1, fin)
	}
	return aux(arr, ini, medio)
}