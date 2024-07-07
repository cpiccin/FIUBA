package main


import (
	"fmt"
	TDACompFunc "TDAs/compFunciones"
)

func main() {
	var suma_dos func(float64) float64 = suma_dos
	var Cuadrado func(float64) float64 = cuadrado


	var a float64 = 1 
	var b float64 = 2

	nueva_composicion := TDACompFunc.CrearComposicion()
	nueva_composicion.AgregarFuncion(suma_dos)
	nueva_composicion.AgregarFuncion(Cuadrado)
	
	a = nueva_composicion.Aplicar(a)
	b = nueva_composicion.Aplicar(b)

	fmt.Println("DESPUES DE LA COMPOSICION: ",a, b)
}


func suma_dos(a float64) float64 {
	return a + 2
}

func cuadrado(a float64) float64 {
	return a * a
}

