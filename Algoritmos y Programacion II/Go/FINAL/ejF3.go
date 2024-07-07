// Implementar un algoritmo que dado un arreglo de dígitos (0-9) determine cuál es el número más grande que se puede
// formar con dichos dígitos.
package main 

import (
	"strings"
	"strconv"
	"fmt"
)

func numMasGrande(digitos []int) int {
	arr := CountingSort(digitos, 11)
	fmt.Println(arr)
	cadNum := make([]string, len(arr))
	for i := range arr {
		num := strconv.Itoa(arr[i])
		cadNum[len(arr)-1-i] = num
	}
	newCad := strings.Join(cadNum, "")
	res, _ := strconv.Atoi(newCad)
	return res 
}

func CountingSort(arr []int, k int) []int {
	res := make([]int, len(arr))
	count := make([]int, k)
	fmt.Println(res, count)
	for i := 0; i < len(arr); i++ {
		count[arr[i]]++
	}
	for suma, i := 0, 0; i < k; i++ {
		suma, count[i] = suma + count[i], suma
	}
	fmt.Println(count)
	for i := range arr {
		res[count[arr[i]]] = arr[i]
		count[arr[i]]++
	}
	return res 
}

func main() {
	arr := []int{9,5,2,0,7}
	fmt.Println(numMasGrande(arr))
}