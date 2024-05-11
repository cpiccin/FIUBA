package main

import (
	"fmt"
	"tda_fraccion"
)

func main() {
    f1 := f.Fraction{numerador: 2, denominador: 3}
    f2 := f.Fraction{numerador: 3, denominador: 4}

    fmt.Println("Fraction 1:", f1)
    fmt.Println("Fraction 2:", f2)

    sum := f1.Sum(f2)
    fmt.Println("Sum:", sum)

    product := f1.Multiply(f2)
    fmt.Println("Product:", product)
}