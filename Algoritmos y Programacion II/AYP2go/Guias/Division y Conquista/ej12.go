// Implementar un algoritmo que, por división y conquista, permita obtener la parte 
// entera de la raíz cuadrada de un número n, en tiempo O(log n)
// Por ejemplo, para n = 10 debe devolver 3, y para n = 25 debe devolver 5

package main

import "fmt"


func main() {
	fmt.Println(RaizEntera(25))
	fmt.Println(RaizEntera(10))
	//anda
}

// pienso en busqueda binaria modificada
func RaizEntera(n int) int {
	return RaizEnteraRec(0, n, n)
}

func RaizEnteraRec(ini, fin, n int) int {
	medio := (ini + fin)/2
	sig := medio + 1

	if medio*medio <= n && sig*sig > n{
		return medio
	}
	
	if medio*medio > n { // significa que me pase y la raiz es mas chica, miro la mitad izq
		return RaizEnteraRec(ini, medio, n)
	}
	
	return RaizEnteraRec(medio, fin, n)
}

// es O(log n)? 
// A = 1 porque no siempre hace los dos llamados recursivos
// B = 2 se parte al medio el intervalo
// C = 0 el resto de operaciones son O(1)
// log 1 = 0 entonces log_B(A) = C = 0 entonces O(log n)