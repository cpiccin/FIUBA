// Dada una lista enlazada implementada con las siguientes estructuras:

     // type nodoLista[T any] struct {
     //     prox *nodoLista[T]
     //     dato T
     // }
     // type ListaEnlazada[T any] struct {
     //     prim *nodoLista[T]
     // }

// Escribir una primitiva de lista que devuelva el elemento que esté a k posiciones del final (el ante-k-último), 
// recorriendo la lista una sola vez y sin usar estructuras auxiliares. 
// Considerar que k es siempre menor al largo de la lista. 

// Por ejemplo, si se recibe la lista [ 1, 5, 10, 3, 6, 8 ], y k = 4, debe devolver 10. 
// Indicar el orden de complejidad de la primitiva.


package main 

import (
    "fmt"
)

type nodoLista[T any] struct {
    prox *nodoLista[T]
    dato T
}
type ListaEnlazada[T any] struct {
    prim *nodoLista[T]
}

func CrearListaEnlazada[T any]() Lista[T] {
    return new(listaEnlazada[T])
}

func (l *listaEnlazada) ante_k_ultimo[T any](k int) T {

    var cont int
    n1, n2 = l.prim, l.prim

    for i := 0; i < k; i++ {
        // lo avanzo hasta k, n1 y n2 siempre van a estar a una distancia k
        n1 = n1.prox
    }

    for n1 != nil {
        n1 = n1.prox
        n2 = n2.prox
    }
    
    return n2.dato
}