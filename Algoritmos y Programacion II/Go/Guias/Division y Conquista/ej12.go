// Implementar un algoritmo que, por división y conquista, permita obtener la parte entera de la raíz
// cuadrada de un número O(logn).
// Por ejemplo, para n = 10 debe devolver 3, y para n = 25 debe devolver 5


package main

import "fmt"

func main() {
	fmt.Println(parteEnteraRaizCuadrada(10))
}

func parteEnteraRaizCuadrada(n int) int {
	return aux(n, 0 , n)
}

func aux(n, ini, fin int) int {
	m := (ini+fin)/2
	if m*m > n {
		return aux(n, ini, m-1)
	}
	if  m*m <= n && (m+1)*(m+1) > n {
		return m
	}
	return aux(n, m, fin)
}