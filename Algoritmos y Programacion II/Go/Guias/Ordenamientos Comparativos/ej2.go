package main

// Implementar un algoritmo que permita ordenar de menor a mayor en O(n) un arreglo casi ordenado de mayor a menor.

import "fmt"

func main() {
	arr := []int{6, 5, 3, 4, 2, 1}
	fmt.Println(arr)
	OrdenaCasiOrdenado(arr)
	fmt.Println(arr)
}

func OrdenaCasiOrdenado(arr []int) {
	for i := 0; i < len(arr); i++ {
		n := arr[i]
		j := i - 1
		for j >= 0 && arr[j] < n{
			arr[j+1] = arr[j]
			j--
		}
		arr[j+1] = n
	}
	for i := 0; i < len(arr)/2; i++ {
		fmt.Println(i)
		arr[i], arr[len(arr)-i-1] = arr[len(arr)-i-1], arr[i]
	}
}

