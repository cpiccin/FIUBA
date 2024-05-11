package main

import (
	"fmt"
	TDAPila "TDAs/pila"
)


func main() {
	pila := TDAPila.CrearPilaDinamica[int]()
	pila.Apilar(3)
	pila.Apilar(2)
	pila.Apilar(1)
	fmt.Println(EsPiramidal(pila))
}

func EsPiramidal(pila TDAPila.Pila[int]) bool {
   
    pila_aux := TDAPila.CrearPilaDinamica[int]()
	var res bool = true 
	n := pila.Desapilar()
	
	if pila.EstaVacia() { // o sea la pila tenia un solo elemento
		return res
	}
	pila.Apilar(n)

	for ! pila.EstaVacia() {
		pila_aux.Apilar(pila.Desapilar())
		if ! pila.EstaVacia() && pila.VerTope() <= pila_aux.VerTope() {
			res = false
		}
	}

	for ! pila_aux.EstaVacia() {
		pila.Apilar(pila_aux.Desapilar())
	}


	return res

}