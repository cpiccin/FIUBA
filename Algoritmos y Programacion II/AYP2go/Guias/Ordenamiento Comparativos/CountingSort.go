package main


import "fmt"


func CountingSort(arr []int, k int) []int {

	count := make([]int, k)
	res := make([]int, len(arr))

	for i := 0; i < len(arr); i++ {
		count[arr[i]]++
	}

	for i, suma := 0, 0; i < k; i++ {
		suma, count[i] = suma+count[i], suma
	}

	for i := range arr {
		res[count[arr[i]]] = arr[i]
		count[arr[i]]++
	}
	return res
}