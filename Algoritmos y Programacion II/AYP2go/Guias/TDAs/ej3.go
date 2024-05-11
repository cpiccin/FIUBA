package main

import (
	"fmt"
	TDAPila "TDAs/pila"
)


func main() {
	var arr1 []int = []int{1,2,3,4}
	fmt.Println(arr1)
	arr1 = invertir_arr(arr1)
	fmt.Println(arr1)
}

func invertir_arr[T any](arr []T) []T {
	pila := TDAPila.CrearPilaDinamica[T]()
	n := len(arr)
	for i := 0; i < n; i++ {
		pila.Apilar(arr[i])
	}
	for i := 0; i<n; i++ {
		arr[n-(n-i)] = pila.Desapilar()
	}
	return arr
}

