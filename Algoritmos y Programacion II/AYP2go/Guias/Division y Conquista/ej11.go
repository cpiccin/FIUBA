package main

import "fmt"

func main() {
	var arr1 []int = []int{1,0,1,1,1,1}
	fmt.Println(arr1)
	fmt.Println(IndicePrimeroCero(arr1))
}

// Se tiene un arreglo tal que [1, 1, 1, ..., 0, 0, ...] (es decir, unos seguidos de
// ceros). Se pide:
// 		a)Una función de orden O(log n) que encuentre el índice del primer 0. 
// 		  Si no hay ningún 0 (solo hay unos), debe devolver -1.
//		b)Demostrar con el Teorema Maestro que la función es O(log n)


func IndicePrimeroCero(arr []int) int {
    if len(arr) == 0{
        return -1
    }
    return indice(arr,0,len(arr)-1)
}

func indice(arr []int, inicio, fin int) int {
    if inicio > fin{
        return -1
    }
    medio := (inicio+fin)/2
    if arr[medio] == 0{
        if inicio == fin || len(arr[inicio:fin])==1 || arr[medio-1]==1{
            return medio
        }
        
        arr_izq := indice(arr,inicio,medio-1)
        return arr_izq
    }
    arr_der := indice(arr,medio+1,fin)
    return arr_der
}