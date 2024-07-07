// Implementar, por división y conquista, una función que determine el mínimo de un arreglo. 
// Indicar y justificar el orden.

package main 

import "fmt"

func main() {
	arr := []int{5, -2, 9, 11, -2, 4, 13}
	fmt.Println(minimo(arr))
}

func minimo(arr []int) int {
	return min(arr, 0, len(arr)-1)
}

func min(arr []int, ini, fin int) int {
	if ini == fin {
		return arr[ini]
	}
	medio := (ini+fin)/2
	izq := min(arr, ini, medio)
	der := min(arr, medio+1, fin)
	if izq < der {
		return izq
	}
	return der
}
