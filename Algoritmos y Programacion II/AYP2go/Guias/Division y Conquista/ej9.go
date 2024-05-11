package main 

import "fmt"

func main() {
	var arr1 []int = []int{0}
	fmt.Println(EstaOrdenado(arr1))
}
//  Implementar, por división y conquista, una función que dado un arreglo
// y su largo, determine si el mismo se encuentra ordenado. 
// Indicar y justificar el orden.

func EstaOrdenado(arr []int) bool {
	if len(arr) == 1 || (len(arr) == 2 && arr[0] <= arr[1]) { 
		return true
	} else if len(arr) == 2 && arr[0] > arr[1] {
		return false
	}
	medio := len(arr)/2
	izq := EstaOrdenado(arr[:medio])
	der := EstaOrdenado(arr[medio:])
	if izq == false || der == false {
		return false
	}
	return arr[medio-1] <= arr[medio]
}
// Complejidad: 
// T(n) = 2 * T(n/2) + O(1)
// A = 2; B = 2; C = 0
// log(2)/log(2) = 1    >   C = 0
// T(n) = O(n^(log_2(2))) = O(n^1) = O(n)                 


