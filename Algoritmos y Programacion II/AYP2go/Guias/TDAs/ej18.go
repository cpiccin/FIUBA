package main 

import (
	"fmt"
	TDAPila "TDAs/pila"
)

func main() {
	pila := TDAPila.CrearPilaDinamica[int]()
	pila.Apilar(1)
	pila.Apilar(2)
	pila.Apilar(3)
	pila.Apilar(4)
	fmt.Println(pila)
	fmt.Println(Largo(pila))
	fmt.Println(pila)
}


func Largo[T any](pila TDAPila.Pila[T]) int {
	pila_aux := TDAPila.CrearPilaDinamica[T]()
	return aux(pila, pila_aux, 0)
}

func aux[T any](pila, pila_aux TDAPila.Pila[T], n int) int {
	if pila.EstaVacia() {
		return n
	}
	elem := pila.Desapilar()
	pila_aux.Apilar(elem)
	n = aux(pila, pila_aux, n+1)
	pila.Apilar(pila_aux.Desapilar())
	return n
}