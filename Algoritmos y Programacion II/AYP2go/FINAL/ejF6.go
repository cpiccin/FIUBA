package main

import (
	"fmt"
	tda "tdas/lista"
	"strconv"
)

func suma_listas(l1, l2 tda.Lista[int]) tda.Lista[int] {
	digitos1 := ""
	digitos2 := ""
	for iter := l1.Iterador(); iter.HaySiguiente(); iter.Siguiente() {
		digitos1 += strconv.Itoa(iter.VerActual())
	}
	for iter := l2.Iterador(); iter.HaySiguiente(); iter.Siguiente() {
		digitos2 += strconv.Itoa(iter.VerActual())
	}
	n1, _ := strconv.Atoi(digitos1)
	n2, _ := strconv.Atoi(digitos2)
	n_final_cad := strconv.Itoa(n1 + n2)
	res := tda.CrearListaEnlazada[int]()
	for i := range n_final_cad {
		n, _ := strconv.Atoi(string(n_final_cad[i]))
		res.InsertarUltimo(n)
	}
	return res
}

func main() {
	l1 := tda.CrearListaEnlazada[int]()
	l2 := tda.CrearListaEnlazada[int]()
	l1.InsertarUltimo(9)
	l1.InsertarUltimo(1)
	l1.InsertarUltimo(5)
	l2.InsertarUltimo(9)
	l2.InsertarUltimo(6)
	nueva := suma_listas(l1, l2)
	for iter := nueva.Iterador(); iter.HaySiguiente(); iter.Siguiente() {
		fmt.Println(iter.VerActual())
	}
}