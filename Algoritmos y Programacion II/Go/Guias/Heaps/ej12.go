// Implementar un algoritmo que reciba un arreglo de n números, y un número k, y devuelva los k números dentro del arreglo cuya suma sería la
// máxima (entre todos los posibles subconjuntos de k elementos de dicho arreglo). La solución debe ser mejor que O(nlogn) si k << n. 
// Indicar y justificar la complejidad de la función implementada.

package main 

import (
	"fmt"
	tda "tdas/cola_prioridad"
)

// len(arr) = n , k  entero
// devuelve los k numeros del arr cuya suma es la maxima

func main() {
	arr := []int{2,5,7,2,1,0,9,4}
	k := 3
	fmt.Println(sumaMax(arr,k))
}

func sumaMax(arr []int, k int) []int {
	heapAux := tda.CrearHeap(cmpIntMin)
	var res []int
	// heap con los primeros k elemtos del heap es O(k) y como k << n es despreciable
	for i := 0; i < k && i < len(arr); i++ {
		heapAux.Encolar(arr[i])
	}

	for i := k; i < len(arr); i++ {
		// veo el resto del arr
		if arr[i] > heapAux.VerMax() {
			// si el elemento que estoy viendo es mayor que el minimo del heap lo reemplazo
			heapAux.Desencolar()
			heapAux.Encolar(arr[i])
		}
	}
	for ! heapAux.EstaVacia() {
		res = append(res, heapAux.Desencolar())
	}
	return res
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