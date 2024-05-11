package main

import "fmt"

func main() {
    var a []int = []int{-3,1,3,4,6,7,8,9}
    fmt.Println(ArregloEsMagico(a))
}



func ArregloEsMagico(arr []int) bool {
    return arregloEsMagico(arr, 0, len(arr)-1)
}

func arregloEsMagico(arr []int, inicio int, fin int) bool {
    fmt.Println(arr[inicio:fin])
    fmt.Println("ini/fin: ", inicio, fin)
    if inicio > fin {
        fmt.Println("ini/fin: ", inicio, fin)
        return false
    }
    medio := (inicio + fin) / 2
    fmt.Println("medio: ", medio)
    if arr[medio] == medio {
        fmt.Println("arr[medio]: ", medio)
        return true
    }
    fmt.Println(arr[medio], " < ", medio)
    if (arr[medio] < medio) {
        fmt.Println(arr[medio], " < ", medio)
        return arregloEsMagico(arr, medio + 1, fin);
    } else {
        return arregloEsMagico(arr, inicio, medio - 1);
    }
}