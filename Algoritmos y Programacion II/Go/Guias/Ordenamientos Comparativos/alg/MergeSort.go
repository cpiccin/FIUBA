package main


import "fmt"


func main() {
    var a []int = []int{2,3,3939,323,4,3,5,75,7}
    fmt.Println(a)
    fmt.Println(MergeSort(a))
}

func MergeSort(arr []int) []int {
    if len(arr) <= 1 {
        return arr
    }
    middle := len(arr) / 2
    left := MergeSort(arr[:middle])
    right := MergeSort(arr[middle:])
    return merge(left, right)
}

func merge(left, right []int) []int {
    r := make([]int, len(left)+len(right))
    for i := 0; ; i++ {
        if len(left) > 0 && len(right) > 0 {
            // pick one smaller item when two arrays are both non-empty
            if left[0] > right[0] {
                r[i] = right[0]
                right = right[1:]
            } else {
                r[i] = left[0]
                left = left[1:]
            }
        } else if len(left) > 0 {
            copy(r[i:], left)
            break
        } else if len(right) > 0 {
            copy(r[i:], right)
            break
        }
    }
    return r
}