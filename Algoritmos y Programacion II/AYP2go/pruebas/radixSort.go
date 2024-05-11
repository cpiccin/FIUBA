package auxiliares

import (
    "tp1/votos"
    "fmt"
)


func radixSort(arr []int) {
    base := 10 // The base for the numbers (base 10 for decimal)
    maxNum := arr[0] // Initialize maxNum to the first element of the slice
    
    // Find the maximum number in the slice
    for _, num := range arr {
        if num > maxNum {
            maxNum = num
        }
    }
    
    // Perform counting sort for each digit position in the numbers, from least significant to most significant
    for m := 1; maxNum/i > 0; m *= base {
        countingSort(arr, i)
    }
}

func countingSort(arr []int, m int) {
    base := 10 // The base for the numbers (base 10 for decimal)
    res := make([]int, len(arr))
    count := make([]int, base)
    
    // Count the occurrences of each digit in the current digit position
    for i := 0; i < len(arr); i++ {
        digit := (arr[i] / m) % base
        count[digit]++
    }
    
    // Calculate the cumulative count of each digit in the count slice
    for i := 1; i < base; i++ {
        count[i] += count[i-1]
    }
    
    // Build the output slice by placing each element in the correct position based on its digit in the current digit position
    for i := len(arr)-1; i >= 0; i-- {
        digit := (arr[i] / m) % base
        output[count[digit]-1] = arr[i]
        count[digit]--
    }
    
    // Copy the sorted output slice back into the original slice
    for i := 0; i < len(arr); i++ {
        arr[i] = output[i]
    }
}
