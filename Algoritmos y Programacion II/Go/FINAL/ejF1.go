// Implementar en Go un algoritmo de RadixSort para ordenar un arreglo de Alumnos (estructuras) en función de sus notas '
// en parcialitos, de menor a mayor. Los alumnos tienen su nombre y las notas (numéricas, 0-10) de los 3 parcialitos.
// El arreglo debe quedar ordenado primero por el promedio de notas. No importan los decimales, nada más la parte entera del promedio.
// Luego, en caso de igualdad en este criterio, los alumnos deben quedar ordenados por la nota del parcialito 1, en caso de persistir 
// la igualdad, la del parcialito 2, y finalmente por la del 3. 


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


// promedio -> p1 -> p2 -> p3

func radixAlumnos(arr []alumnos) []alumnos {
	arr = CountingSort(arr, 11, "3")
	arr = CountingSort(arr, 11, "2")
	arr = CountingSort(arr, 11, "1")
	arr = CountingSort(arr, 11, "0")
	return arr 
}

func CountingSort(arr []alumnos, k int, criterio int) []alumnos {
	res = make([]alumnos, len(arr))
	count = make([]int, k)

	for i := 0; i < len(arr); i++ {
		pos := pos(criterio, arr[i])
		count[pos]++
	}
	for suma, i := 0, 0; i < k; i++ {
		suma, count[i] = suma + count[i], suma 
	}
	for i := range arr {
		pos := pos(criterio, arr[i])
		res[count[pos]] = arr[i]
		count[pos]++
	}
	return res
}


func pos(criterio string, alumno alumnos) int {
	if criterio == "3" {return alumno.Nota(3)}
	if criterio == "2" {return alumno.Nota(2)}
	if criterio == "1" {return alumno.Nota(1)}
	return alumno.Promedio()
}