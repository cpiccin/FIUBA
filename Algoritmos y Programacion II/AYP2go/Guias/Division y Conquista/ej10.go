package main

import "fmt"

// Implementar, por división y conquista, una función que dado un arreglo sin elementos 
// repetidos y casi ordenado (todos los elementos se encuentran ordenados, salvo uno), 
// obtenga el elemento fuera de lugar. Indicar y justificar el orden.


func main() {
	var arr []int = []int{2,1,3,4,5,6}
	fmt.Println(FueraDeLugar(arr))
}

func FueraDeLugar(arr []int) int {
	return fueraDeLugar(arr, 0, len(arr)-1)
}

func fueraDeLugar(arr []int, ini, fin int) int {
    
}