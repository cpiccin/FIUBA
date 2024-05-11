// Se tiene un arreglo de n>=3 elementos en forma de pico, esto es: estrictamente creciente hasta una
// determinada posición p, y estrictamente decreciente a partir de ella (con 0<p<n-1)
// Por ejemplo, en el arreglo [1, 2, 3, 1, 0, -2] la posición del pico es p=2. 
// Se pide:
// Implementar un algoritmo de división y conquista de orden O(logn) que encuentre la posición del pico: 
// func PosicionPico(v []int, ini, fin int) int. 
// La función será invocada inicialmente como: PosicionPico(v, 0, len(v)-1), y tiene como pre-condición que 
// el arreglo tenga forma de pico.
// Justificar el orden del algoritmo mediante el teorema maestro.

package main

import "fmt"

func main() {
	v := []int{1,2,3,4,5,-2}
	fmt.Println(PosicionPico(v, 0, len(v)-1))
}

func PosicionPico(v []int, ini, fin int) int {
	if ini == fin || (fin-ini) <= 1 {
		return fin
	}
	medio := (ini+fin)/2
	if v[medio] > v[medio-1] && v[medio] < v[medio+1] {
		return PosicionPico(v, medio, fin)
	}
	if v[medio-1] < v[medio] && v[medio] > v[medio+1] {
		return medio
	}
	return PosicionPico(v, ini, medio-1)
}

func PosicionPico(v []int, ini, fin int) int {
    medio := (ini+fin)/2
    if v[medio] < v[medio+1] {
        return PosicionPico(v, medio, fin)
    }
    if v[medio] < v[medio-1] {
        return PosicionPico(v, ini, medio)
    }
    return medio
}