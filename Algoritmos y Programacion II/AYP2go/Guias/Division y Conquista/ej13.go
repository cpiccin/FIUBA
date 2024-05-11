package main

import "fmt"

func main() {

}

func PosicionPico(v []int, ini, fin int) int {
	if ini == fin {
		return ini
	}
	medio := (ini+fin)/2
	if v[medio] < v[medio+1] {
		return PosicionPico(v, medio+1, fin)
	}
	return PosicionPico(v, ini, medio)
}