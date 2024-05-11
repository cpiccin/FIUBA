package main 

import (
	"fmt"
	tda "tdas/diccionario"
)

func main() {
	arbol := tda.CrearABB[int, string](func (a, b int) int {
		return a - b
	})
	arbol.Guardar(12, "")
	arbol.Guardar(7, "")
	arbol.Guardar(15, "")
	arbol.Guardar(5, "")
	arbol.Guardar(9, "")
	arbol.Guardar(6, "")
	arbol.Guardar(3, "")
	arbol.Guardar(4, "")
	arbol.Guardar(17, "")
	arbol.Guardar(16, "")
	arbol.Guardar(19, "")
	arbol.Guardar(18, "")
	arbol.Guardar(23, "")
	fmt.Println(arbol.RecorridoNivelesInverso())
}