package main

// Implementar una función que reciba un arreglo genérico e invierta su orden, utilizando los TDAs vistos. 
// Indicar y justificar el orden de ejecución.

import (
    "fmt"
    tda "tdas/pila"
)

func main() {
    arreglo := []string{"papa", "banana", "cebolla", "zapallo", "brocoli", "tomate", "lechuga"}
    fmt.Println(arreglo)
    InvierteOrden(arreglo)
    fmt.Println(arreglo)
}


func InvierteOrden[T any](arr []T) {
    pilaAux := tda.CrearPilaDinamica[T]()

    for i := 0; i < len(arr); i++ {
        pilaAux.Apilar(arr[i])
    }
    for i := 0; i < len(arr); i++ {
        arr[i] = pilaAux.Desapilar()
    }
}