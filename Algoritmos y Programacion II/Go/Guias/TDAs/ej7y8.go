// Implementar la primitiva func (cola *colaEnlazada[T]) Multiprimeros(k int) []T que dada una cola y un número 
// k, devuelva los primeros k elementos de la cola, en el mismo orden en el que habrían salido de la cola. 
// En caso que la cola tenga menos de k elementos. Si hay menos elementos que k en la cola, devolver un slice del 
// tamaño de la cola. 
// Indicar y justificar el orden de ejecución del algoritmo.

package main

import (
    tda "tdas/pila"
)

// Primitiva
func (cola *colaEnlazada[T]) Multiprimeros(k int) []T {
    colaAux := CrearColaEnlazada[T]()
    var res []T

    for i := 0; ! cola.EstaVacia(); i++ {
        elem := cola.Desencolar()

        if i < k {
            res = append(res, elem)
        }

        colaAux.Encolar(elem)
    }

    for ! colaAux.EstaVacia() {
        cola.Encolar(colaAux.Desencolar())
    }
    
    return res
}

// Funcion
func Multiprimeros[T any](cola Cola[T], k int) []T {
    colaAux := CrearColaEnlazada[T]()
    var res []T

    for i := 0; ! cola.EstaVacia(); i++ {
        elem := cola.Desencolar()

        if i < k {
            res = append(res, elem)
        }

        colaAux.Encolar(elem)
    }

    for ! colaAux.EstaVacia() {
        cola.Encolar(colaAux.Desencolar())
    }
    
    return res
}