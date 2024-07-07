// Implementar una función (que utilice división y conquista) de orden O(nlogn) que dado un arreglo de 
// n números enteros devuelva true o false según si existe algún elemento que aparezca más de la mitad 
// de las veces. Justificar el orden de la solución. Ejemplos:

// [1, 2, 1, 2, 3] -> false
// [1, 1, 2, 3] -> false
// [1, 2, 3, 1, 1, 1] -> true
// [1] -> true

package main

func MasDeLaMitad(arr []int) bool {
	if aux(arr, 0, len(arr)-1) > 0 {
		return true
	}
	return false
}

func aux(arr []int, ini, fin int) int {
	if ini == fin {
		return arr[ini]
	}
	
	medio := (ini+fin)/2
	izq := aux(arr, ini, medio)
	der := aux(arr, medio+1, fin)

	contIzq := contarApariciones(arr, izq, ini, fin)
	contDer := contarApariciones(arr, der, ini, fin)

	if contIzq > (fin-ini+1)/2 {
		return izq
	} else if contDer > (fin-ini+1)/2 {
		return der 
	}
	return -1
}

func contarApariciones(arr []int, n, ini, fin int) int {
	cont := 0
	for i := ini; i <= fin; i++ {
		if arr[i] == n {
			cont++
		}
	}
	return cont
}