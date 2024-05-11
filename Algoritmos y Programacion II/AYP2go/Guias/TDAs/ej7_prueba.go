package main

import (
	"fmt"
	TDACola "TDAs/cola"
)

func main() {
	cola := TDACola.CrearColaEnlazada[int]()
	cola.Encolar(1)
	cola.Encolar(2)
	cola.Encolar(3)
	cola.Encolar(4)
	cola.Encolar(5)
	k := 1
	arr_k := cola.Multiprimeros(k)
	fmt.Println(arr_k)
}