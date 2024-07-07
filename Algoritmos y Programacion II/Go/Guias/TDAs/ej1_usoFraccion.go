package main

import (
	"fmt"
	TDAFraccion "TDAs/fraccion"
)


func main() {
	fraccion1 := TDAFraccion.CrearFraccion(2, 5)
	fraccion2 := TDAFraccion.CrearFraccion(6, 2)
	suma_fracciones := fraccion1.Sumar(fraccion2)
	fmt.Print(suma_fracciones.Representacion())
	mult_fracciones := fraccion1.Multiplicar(fraccion2)
	fmt.Print(mult_fracciones.Representacion())
	fmt.Println(fraccion1.ParteEntera())
	fmt.Println(fraccion2.ParteEntera())
}