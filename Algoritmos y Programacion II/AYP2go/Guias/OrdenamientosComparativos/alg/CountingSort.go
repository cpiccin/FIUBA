package main


import "fmt"


func CountingSort(arr []int, k int) []int {

	count := make([]int, k)
	res := make([]int, len(arr))
	//cuento frecuencias
	for i := 0; i < len(arr); i++ {
		count[arr[i]]++
	}
	//suma acumulativa
	for i, suma := 0, 0; i < k; i++ {
		suma, count[i] = suma+count[i], suma
	}
	//ordeno en el res segun lo que diga la suma acumulativa
	for i := range arr {
		res[count[arr[i]]] = arr[i]
		count[arr[i]]++
	}
	return res
}