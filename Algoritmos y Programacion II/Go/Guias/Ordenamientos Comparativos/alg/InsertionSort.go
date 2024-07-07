package main


import "fmt"


func main() {
    var a []int = []int{2,4,3,3,5,4,39393,4,3,323,4,3,5,4,6,5,75,7,5}
    fmt.Println(a)
    fmt.Println(InsertionSort(a))
}

func InsertionSort(arr []int) []int {
    for i := 0; i < len(arr); i++ {
        for j := i; j < len(arr); j++ {
            if arr[i] > arr[j] {
                arr[i], arr[j] = arr[j], arr[i]
            }
        }
    }
    return arr
}