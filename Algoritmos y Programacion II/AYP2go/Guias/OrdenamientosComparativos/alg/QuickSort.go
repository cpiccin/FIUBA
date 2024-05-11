package main


import "fmt"


func main() {
    var a []int = []int{2,3,1,34,4,234,2,2,3,5}
    fmt.Println(a)
    fmt.Println(QuickSort(a))
}

func QuickSort(arr []int) []int {
    return quickSort(arr, 0, len(arr)-1)
}

func quickSort(arr []int, ini, fin int) []int {
    if ini < fin {
        // fmt.Println("EN quickSort ini/fin: ", ini, fin,"\n")
        pivot := partition(arr, ini, fin)
        // fmt.Println("EN quickSort pivote despues de partition: ", pivot)
        quickSort(arr, ini, pivot-1)
        quickSort(arr, pivot+1, fin)
    }
    return arr
}

func partition(arr []int, ini, fin int) int {
    pivot := arr[fin]
    i := ini
    // fmt.Println("inicio i: ", i, "pivote: ", pivot)
    for j := ini; j < fin; j++ {
        // fmt.Println("arr principio del for: ", arr, "  j: ", j)
        if arr[j] <= pivot {
            // fmt.Println("en el if donde ", arr[j], "<=", pivot)
            arr[i], arr[j] = arr[j], arr[i]
            i++
            // fmt.Println("i aumenta: ", i)
        }
    }
    // cuando se termina de iterar se mueve el pivote a donde corresponde
    arr[i], arr[fin] = arr[fin], arr[i]
    // fmt.Println("arr cuando termina el for: ", arr, "\n")
    return i
}
