package main

import "fmt"

// Swap intercambia dos valores enteros.
func Swap(x *int, y *int) {
	*x, *y = *y, *x

}

func Maximo(vector [4]int) int {

	var maximo int = 0
	var maximoPosicion int

	if len(vector) == 0 {
		return -1
	}

	for i := 0; i < len(vector); i++ {

		if vector[i] > maximo {
			maximoPosicion = i
			maximo = vector[i]
		}
	}
	return maximoPosicion
}

func main() {
	var lista1 []int = []int{1,4,3}
	//var lista2 []int = []int{1, 2}
	fmt.Println(lista1)
	Seleccion(lista1)
	fmt.Println(lista1)
}

// Comparar compara dos arreglos de longitud especificada.
// Devuelve -1 si el primer arreglo es menor que el segundo; 0 si son iguales; o 1 si el primero es el mayor.
// Un arreglo es menor a otro cuando al compararlos elemento a elemento, el primer elemento en el que difieren
// no existe o es menor.
func Comparar(vector1 []int, vector2 []int) int {

	for i := 0; i < len(vector1) && i < len(vector2) ; i++ {
		if vector1[i] > vector2[i] {
			return 1
		} else if vector1[i] < vector2[i] {
			return -1
		} else {
			continue
		}
	}
	
	if len(vector1) > len(vector2) {
		return 1
	} else if len(vector1) < len(vector2) {
		return -1
	}
	return 0
}


func Seleccion(vector []int) {

	var n int = len(vector)-1

	for i:=n; i>0; {

		var max_actual int = 0
		
		for j:=1; j<(i+1); j++ {
			if vector[j] > vector[max_actual] {
				max_actual = j
			}
		}
		vector[max_actual], vector[i] = vector[i], vector[max_actual]   
		i--                 
		}
}