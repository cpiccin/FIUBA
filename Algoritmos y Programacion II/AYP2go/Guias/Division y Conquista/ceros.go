package main


import "fmt"

func main() {
	var a []int = []int{1}
	fmt.Println("array: ",a)
	fmt.Println("funcion: ",ceros(a))
}


func ceros(vector []int) int {
	if len(vector) == 0 {
		return 0
	} else if len(vector) == 1 && vector[0] == 0 {
		return 1
	} 
	return aux(vector, 0, 0, len(vector)-1)
}

func aux(arr []int, n, ini, fin int) int {
	
	if ini > fin { 
		return 0
	}

	medio := (ini+fin)/2

	if arr[medio] == 0 {
		if  arr[medio-1] == 1 {
			return len(arr) - medio
		}
		return aux(arr, n, ini, medio-1)
	}
	return aux(arr, n, medio+1, fin)
}


