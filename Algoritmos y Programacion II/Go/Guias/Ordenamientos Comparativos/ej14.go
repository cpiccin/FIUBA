// Implementar en Go un algoritmo de RadixSort para ordenar un arreglo de Alumnos (estructuras) en función de sus notas '
// en parcialitos, de menor a mayor. Los alumnos tienen su nombre y las notas (numéricas, 0-10) de los 3 parcialitos.
// El arreglo debe quedar ordenado primero por el promedio de notas. No importan los decimales, nada más la parte entera del promedio.
// Luego, en caso de igualdad en este criterio, los alumnos deben quedar ordenados por la nota del parcialito 1, en caso de persistir 
// la igualdad, la del parcialito 2, y finalmente por la del 3. 


package main 

import "fmt"

func main() {
	a1, a2, a3, a4, a5, a6, a7 := []int{2,2,2}, []int{8,4,6}, []int{4,5,6}, []int{2,2,3}, []int{9,8,3}, []int{4,5,4}, []int{9,9,2}
	arr := []alumnos{CrearAlumno("CP", a1), CrearAlumno("NP", a2), CrearAlumno("AD", a3), CrearAlumno("MG", a4), CrearAlumno("SA", a5), CrearAlumno("HD", a6), CrearAlumno("CZ", a7)}
	fmt.Println(Radix(arr))
}	


type alumnos struct {
	nombre string 
	notas []int
}

func CrearAlumno(nombre string, notas []int) alumnos {
	return alumnos{nombre: nombre, notas: notas}
}

func (a alumnos) Nota(parcial int) int {
	// devuelve la nota del parcial recibido
	return a.notas[parcial-1]
}

func (a alumnos) Promedio() int {
	suma := a.notas[0] + a.notas[1] + a.notas[2]
	return suma/3
}


func Radix(arr []alumnos) []alumnos {
	// primero ordeno segun notas de parciales
	arr = CountingSort(arr, 11, "3") // parcial 1
	arr = CountingSort(arr, 11, "2") // parcial 2
	arr = CountingSort(arr, 11, "1") // parcial 3
	// despues ordeno segun promedio con un algoritmo estable
	arr = CountingSort(arr, 11, "promedio")
	return arr
}

func CountingSort(arr []alumnos, k int, criterio string) []alumnos {
	count := make([]int, k)
	res := make([]alumnos, len(arr))

	for i := 0; i < len(arr); i++ {
		pos := pos(arr[i], criterio)
		count[pos]++
	}
	for i, suma := 0, 0; i < k; i++ {
		suma, count[i] = suma + count[i], suma 
	}
	for i := range arr {
		pos := pos(arr[i], criterio)
		res[count[pos]] = arr[i]
		count[pos]++
	}
	return res 
}

func pos(i alumnos, criterio string) int {
	if criterio == "promedio" {
		return i.Promedio()
	} else if criterio == "1" {
		return i.Nota(1)
	} else if criterio == "2" {
		return i.Nota(2)
	} else {
		return i.Nota(3)
	}
}