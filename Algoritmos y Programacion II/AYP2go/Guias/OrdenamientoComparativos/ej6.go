package main

// Realizar el seguimiento de ordenar por Radix Sort el siguiente arreglo de cadenas que representan versiones. 
// Cada versión tiene el formato a.b.c, donde cada valor a, b y c puede tener un valor entre 0 y 99. 
// Considerar que se quiere que quede ordenado primero por la primera componente (a), luego por la segunda (b) 
// y finalmente por la tercera (c). Se puede asumir que a nunca será 0 salvo que el número sea efectivamente 0. 
// Es decir, la notación es correcta. Tener en cuenta que, por ejemplo 1.1.3 < 1.1.20, 2.20.8 < 3.0.0.

// ["4.3.2", "5.1.2", "10.1.4", "2.1.20", "2.2.1", "4.2.3", "2.1.5", "8.1.2", "5.30.1", "10.0.23"]

import (
	"fmt"
	"strconv"
	"strings"
)

func main() {
	arr := []string{"4.3.2", "5.1.2", "10.1.4", "2.1.20", "2.2.1", "4.2.3", "2.1.5", "8.1.2", "5.30.1", "10.0.23"}
	fmt.Println(arr)
	fmt.Println(Radix(arr))
}

func Radix(arr []string) []string {
	// hay que ordenar de la menos significativa a la mas significativa
	// de c->b->a
	arr = CountingSort(arr, 99, 2) // ordenado segun c
	arr = CountingSort(arr, 99, 1) // ordenado segun b
	arr = CountingSort(arr, 99, 0) // ordenado segun a
	return arr
}

func CountingSort(arr []string, k int, cifra int) []string {
	count := make([]int, k+1)
	res := make([]string, len(arr))

	for i := 0; i < len(arr); i++ {
		cad := strings.Split(arr[i], ".")[cifra]
		pos, _ := strconv.Atoi(cad)
		count[pos]++
	}
	for i, suma := 0, 0; i < k+1; i++ {
		suma, count[i] = suma + count[i], suma 
	}
	for i := range arr {
		cad := strings.Split(arr[i], ".")[cifra]
		pos, _ := strconv.Atoi(cad)
		res[count[pos]] = arr[i]
		count[pos]++
	}
	return res
}