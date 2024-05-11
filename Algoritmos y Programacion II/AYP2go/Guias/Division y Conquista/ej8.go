package main

import "fmt"

func main() {
    arr := []int{10, 2}
    fmt.Println(BuscarMinimo(arr))
}


func BuscarMinimo(arr []int) int {
    if len(arr) == 1 {
        return arr[0]
    }
    medio := len(arr) / 2
    medio_izq := BuscarMinimo(arr[:medio])
    medio_der := BuscarMinimo(arr[medio:])
    if medio_izq < medio_der {
        return medio_izq
    } else {
        return medio_der
    }
}