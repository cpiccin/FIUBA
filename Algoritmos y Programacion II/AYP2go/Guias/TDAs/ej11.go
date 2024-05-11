package main

import (
    "fmt"
    TDAPila "TDAs/pila"
)

func main() {
    pila := TDAPila.CrearPilaDinamica[int]()
    pila.Apilar(2)
    pila.Apilar(1)
    pila.Apilar(4)
    pila.Apilar(6)
    pila.Apilar(7)
    pila.Apilar(5)
    pila.Apilar(3)
    fmt.Println(pila)
    Ordenar(pila)
    fmt.Println(pila)
}



func Ordenar(pila TDAPila.Pila[int]) {
    aux := TDAPila.CrearPilaDinamica[int]()
    for ! pila.EstaVacia() {
        elem := pila.Desapilar()
        for ! aux.EstaVacia() && aux.VerTope() < elem {
            temp := aux.Desapilar()
            pila.Apilar(temp)
        }
        aux.Apilar(elem)
    }
    for ! aux.EstaVacia() {
        pila.Apilar(aux.Desapilar())
    }
}