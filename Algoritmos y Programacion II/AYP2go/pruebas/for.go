package main

import "fmt"

func main() {
	var lista1 []int = []int{1,2,3,4}
	ciclo(lista1)
	fmt.Println(lista1)
}


func ciclo(lista []int) {
	var n int = len(lista) - 1
	for i := n; i > 0; i-- {
		fmt.Println(i)
	}
	fmt.Println(n)
}	