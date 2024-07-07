package main

import (
	"fmt"
	tda "tdas/cola_prioridad"
)

func main() {
	arr := []int{8, 2, 1, 5, 10, 6, 14, 4}
	heap := tda.CrearHeapArr(arr, cmpIntMin)
	heap.Encolar(6)
	heap.Encolar(3)
	heap.Encolar(17)
	heap.Desencolar()
	heap.Encolar(7)
	heap.Desencolar()
	fmt.Println(heap)
}

func cmpIntMin(n1, n2 int) int {
	// tienen prioridad los int menores
	if n1 < n2 {
		return 1
	}
	if n2 < n1 {
		return -1
	}
	return 0
}