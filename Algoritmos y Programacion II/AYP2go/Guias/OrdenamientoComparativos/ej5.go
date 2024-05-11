package main

// Hacer el seguimiento de counting sort para ordenar por año las siguientes obras:
//     1988 - Crónicas del Ángel Gris
//     2000 - Los Días del Venado
//     1995 - Alta Fidelidad
//     1987 - Tokio Blues
//     2005 - En Picada
//     1995 - Crónica del Pájaro que Da Cuerda al Mundo
//     1995 - Ensayo Sobre la Ceguera
//     2005 - Los Hombres que No Amaban a las Mujeres
// ¿Cuál es el orden del algoritmo? ¿Qué sucede con el orden de los elementos de un mismo año, 
// respecto al orden inicial, luego de finalizado el algoritmo? Justificar brevemente.

import "fmt"

func main() {
	arr := []int{1988,2000,1995,1987,2005,1995,1995,2005}
	min, max := arr[0], arr[0]
	for i := 0; i < len(arr); i++ {
		if arr[i] < min {
			min = arr[i]
		}
		if arr[i] > max {
			max = arr[i]
		}
	}
	k := max-min+1
	arr = CountingSort(arr, min, k)
	fmt.Println(arr)
}

func CountingSort(arr []int, min, k int) []int {
	
	count := make([]int, k)

	for i := 0; i < len(arr); i++ { // O(n)
		pos := arr[i] - min
		count[pos]++
	}
	// suma acumulada
	for i, suma := 0, 0; i < k; i++ { // O(k)
		suma, count[i] = suma + count[i], suma
	}

	res := make([]int, len(arr))
	for i := range arr { // O(n)
		res[count[arr[i] - min]] = arr[i]
		count[arr[i] - min]++
	} 

	return res
}

// El orden es O(n + k)
// Se mantiene el orden relativo