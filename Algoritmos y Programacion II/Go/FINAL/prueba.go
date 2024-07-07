package main

func CountingSort(arr, k) [] {
	res := make([]int, len(arr))
	count := make([]int, k)

	for i := 0; i < len(arr); i++ {
		count[arr[i]]++
	}
	for suma, i := 0, 0; i < len(count); i++ {
		suma, count[i] := suma + count[i], suma 
	}
	for i := range arr {
		res[count[arr[i]]] = arr[i]
		count[arr[i]]++
	}

}