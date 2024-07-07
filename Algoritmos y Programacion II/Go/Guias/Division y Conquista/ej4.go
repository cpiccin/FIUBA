package main

import "fmt"

func main() {
    imprimirDyC(8)
}

func imprimirDyC(m int) {
    if m < 4 {
        return
    }
    fmt.Println(m)
    imprimirDyC(m / 4)
    imprimirDyC(m - (m / 4))
}