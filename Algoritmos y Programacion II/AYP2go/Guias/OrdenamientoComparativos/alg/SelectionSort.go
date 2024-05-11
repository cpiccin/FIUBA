package main


import "fmt"


func main() {
    var a []int = []int{2,4,3,3,5,4,39393,4,3,323,4,3,5,4,6,5,75,7,5}
    fmt.Println(a)
    fmt.Println(SelectionSort(a))
}



func SelectionSort(arr []int) []int {
    for i := 0; i < len(arr)-1; i++ {
        iMin := i
        for j := i + 1; j < len(arr); j++ {
            if arr[j] < arr[iMin] {
                iMin = j
            }
        }
        if iMin != i {
            arr[i], arr[iMin] = arr[iMin], arr[i]
        }
    }
    return arr
}