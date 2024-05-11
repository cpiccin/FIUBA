// Se tiene un arreglo de cadenas que representan fechas 
// de la forma YYYYMMDD (ej: 20110626 representa el 26/06/2011). 
// Implementar un algoritmo lineal que las ordene de forma creciente


package main

import "fmt"

func main() {
	a := []string{"20110626", "20030102", "19980923", "20130702"}
	fmt.Println(a)
	fmt.Println(OrdenarFechas(a))

}

func OrdenarFechas(arr []string) []int {
	arr = ordena(arr, 31, 6, 8) // para la cadena "20110626" es el "26"
	arr = ordena(arr, 12, 4, 6) // "06"
	arr = ordena(arr, 10000, 0, 4) // "2011"
	return arr
}

func ordena(fechas []string, largo, ini, fin int) []int {
	tiempos := make([][]string, largo) // lista de listas

	for i := 0; i < largo; i++ {
		tiempos[i] = []string
	}
	for f := range fechas {
		tiempo := int(fechas[ini:fin])
		tiempos[tiempo] = append(tiempos[tiempo], f)
	}
	indice := 0
	for lista := range tiempos {
		for j := 0; j < len(lista); indice++ {
			fechas[indice] = tiempos[j]
		}
	}
	return tiempos
}