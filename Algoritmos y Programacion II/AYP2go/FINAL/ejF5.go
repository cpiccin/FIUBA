package main

import (
	"fmt"
	tda "tdas/diccionario"
)

type guante struct {
	color int 
	talle int 
}

func (g guante) Color() int {
	return g.color
}

func (g guante) Talle() int {
	return g.talle
}

func main() {
	g1, g2, g3, g4, g5, g6 := guante{color:1, talle:1}, guante{color:2, talle:1}, guante{color:5, talle:1}, guante{color:1, talle:1}, guante{color:5, talle:1}, guante{color:2, talle:1}
	arr := []guante{g1, g2, g3, g4, g5, g6}
	fmt.Println(se_puede(arr))
}

func se_puede(arr []guante) bool {
	diccAux := tda.CrearHash[int, int]()
	if len(arr) % 2 != 0 {
		return false
	}
	for _, guante := range arr {
		if !diccAux.Pertenece(guante.Color()) {
			diccAux.Guardar(guante.Color(), 1)
		} else {
			diccAux.Guardar(guante.Color(), diccAux.Obtener(guante.color)+1)
		}
	}
	for _, guante := range arr {
		n := diccAux.Obtener(guante.Color())
		if n % 2 != 0 {
			return false
		}
	}
	return true
}