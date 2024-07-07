// Tenemos un arreglo de tamaño 2n de la forma {C1, C2, C3, … Cn, D1, D2, D3, … Dn}, tal que la cantidad total de elementos 
// del arreglo es potencia de 2 (por ende, n también lo es). Implementar un algoritmo de División y Conquista que modifique 
// el arreglo de tal forma que quede con la forma {C1, D1, C2, D2, C3, D3, …, Cn, Dn}, sin utilizar espacio adicional (
// obviando el utilizado por la recursividad). ¿Cual es la complejidad del algoritmo?

// Pista: Pensar primero cómo habría que hacer si el arreglo tuviera 4 elementos ({C1, C2, D1, D2}). Luego, pensar a partir 
// de allí el caso de 8 elementos, etc… para encontrar el patrón.

package main 

import "fmt"

func main() {
	arr := []int{1, 3, 5, 7, 2, 4, 6, 8}
	fmt.Println(arr)
	alternado(arr)
	fmt.Println(arr)
}

func alternado(arr []int) {
	aux(arr, 0, len(arr)-1, 1)
}

func aux(arr []int, ini, fin, i int) int {
	if ini == fin {
		return arr[ini]
	}
	medio := (ini+fin)/2
	
	return 
}
