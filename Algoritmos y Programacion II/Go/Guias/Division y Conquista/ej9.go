// Implementar, por división y conquista, una función que dado un arreglo y su largo, determine si 
// el mismo se encuentra ordenado. Indicar y justificar el orden.

package main

import "fmt"

func main() {
	arr := []int{1,4,5,6,7,9,12, 34, 2, 10}
	fmt.Println(estaOrdenado(arr))
}

func estaOrdenado(arr []int) bool {
	return w(arr, 0, len(arr)-1)
}

func w(arr []int, ini, fin int) bool {
	if (fin-ini) <= 1 {
		return true
	}
	fmt.Println(arr[ini:fin])
	medio := (ini+fin)/2
	izq := w(arr, ini, medio)
	der := w(arr, medio+1, fin)
	fmt.Println(medio)
	if arr[medio-1] <= arr[medio] && izq && der {
		return true
	}
	return false
}