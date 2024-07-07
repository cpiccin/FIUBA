// Dadas dos pilas de enteros positivos (con posibles valores repetidos) cuyos elementos fueron ingresados 
// de menor a mayor, se pide implementar una función func MergePilas(pila1, pila2 Pila[int]) []int que 
// devuelva un array ordenado de menor a mayor con todos los valores de ambas pilas sin repeticiones. 
// Detallar y justificar la complejidad del algoritmo considerando que el tamaño de las pilas es N y M
// respectivamente.

// ej de pila [1, 2, 4, 6, 7, 7, 9, 10, 11, 45, 46] <-- Tope

package main 
import (
	"fmt"
	tda "tdas/pila"
)

func main() {
	pila1, pila2 := tda.CrearPilaDinamica[int](), tda.CrearPilaDinamica[int]()
	pila1.Apilar(2)
	pila1.Apilar(4)
	pila1.Apilar(5)
	pila1.Apilar(6)
	pila1.Apilar(6)
	pila1.Apilar(9)
	// pila2.Apilar(1)
	// pila2.Apilar(2)
	// pila2.Apilar(4)
	// pila2.Apilar(9)
	// pila2.Apilar(10)
	fmt.Println(pila1.Representar(), pila2.Representar())
	fmt.Println(MergePilas(pila1, pila2))
}

// CORREGIR 
func MergePilas(pila1, pila2 tda.Pila[int]) []int {
	pilaAux := tda.CrearPilaDinamica[int]()
	var elem int
	
	for ! pila1.EstaVacia() && ! pila2.EstaVacia() {
		tope1, tope2 := pila1.VerTope(), pila2.VerTope()
		
		if tope1 > tope2 {
			elem = pila1.Desapilar()
		} else {
			elem = pila2.Desapilar()
		}
		if pilaAux.EstaVacia() || pilaAux.VerTope() != elem {
			pilaAux.Apilar(elem)
		}
	}


	for ! pila1.EstaVacia() {
		elem = pila1.Desapilar()
		if pilaAux.EstaVacia() || pilaAux.VerTope() != elem  {
			pilaAux.Apilar(elem)
		}
	}
	for ! pila2.EstaVacia() {
		elem = pila2.Desapilar()
		if pilaAux.EstaVacia() || pilaAux.VerTope() != elem  {
			pilaAux.Apilar(elem)
		}
	}

	return pilaALista(pilaAux)
}

func pilaALista(pila tda.Pila[int]) []int {
	res := []int{}
	for ! pila.EstaVacia() {
		res = append(res, pila.Desapilar())
	}
	return res
}

