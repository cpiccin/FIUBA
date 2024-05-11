// Se tiene una larga lista de números de tres cifras abc que representan números en notación científica de la forma: a,b.10^c
// Por ejemplo 123 representaría el número 1,2.10^3
    
//     a) Diseñe un algoritmo para ordenar los números según su valor en notación científica. ¿De qué orden es?

//     b) Muestre cómo se ordena la siguiente lista de números con el algoritmo que diseñó:
//     [122,369,332,180,486,349,326,101] 
//     que representan:
//     [1,2.10^2; 2,6.10^9; 3,2.10^2; 1,8.10^0; 4,8.10^6; 3,4.10^9; 3,2.10^6; 1,0.10^1]
//     y equivalen a:
//     [120;3600000000;330;1,8;4800000;3400000000;3200000;10]

package main 

import "fmt"

func main() {
    arr := []int{122,369,332,180,486,349,326,101}
    fmt.Println(Radix(arr))

}

func Radix(arr []int) []int {
    arr = CountingSort(arr, 10, "b")
    arr = CountingSort(arr, 10, "a")
    arr = CountingSort(arr, 10, "c")
    return arr
}

func CountingSort(arr []int, k int, cifra string) []int {
    count := make([]int, k)
    res := make([]int, len(arr))

    for i := 0; i < len(arr); i++ {
        pos := segunCifra(arr[i], cifra)
        count[pos]++
    }
    for i, suma := 0, 0; i < k; i++ {
        suma, count[i] = suma + count[i], suma 
    }
    for i := range arr {
        pos := segunCifra(arr[i], cifra)
        res[count[pos]] = arr[i]
        count[pos]++
    }
    return res
}

func segunCifra(i int, cifra string) int {
    if cifra == "c" {
        return i%10    
    } else if cifra == "b" {
        return (i%10)/10
    } else {
        return i/100
    }
}


