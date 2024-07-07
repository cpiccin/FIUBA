// Implementar un algoritmo de ordenamiento, que sea lineal, que permita definir el orden en una fila de personas para
// comprar una Cajita CampeónFeliz en un establecimiento de comida rápida. Los datos (structs) a ordenar cuentan con edad
// (número), nombre (string) y nacionalidad (enumerativo, de 32 valores posibles). Primero deben ir los niños (todos con
// edad menor o igual a 12), y estos deben ordenarse por edad (de menor a mayor), independientemente de la nacionalidad.
// Luego deben ir los “no niños”, que primero deben estar ordenados por nacionalidad (segundo Francia, por ejemplo) y en
// caso de igualdad de nacionalidad, por edad, también de menor a mayor. En caso de necesitar algún ordenamiento auxiliar 
// en caso que una parte del algoritmo implique hacer BucketSort o RadixSort), puede considerarse como ya implementado.


package main

import "fmt"

type persona struct {
	edad int 
	//nombre string
	nacionalidad int // enumerativo, del 0 al 32
}

func CrearPersona(edad int, nac int) persona {
	//return persona{edad: edad, nombre: nom, nacionalidad: nac}
	return persona{edad: edad, nacionalidad: nac}
}

func (p persona) Edad() int {return p.edad}
func (p persona) Nacionalidad() int {return p.nacionalidad}

// ordenar segun edad < a 12 y > a 12  ------> MAS SIGNIFICATIVA
// ordenar < a 12 de menor a mayor
// ordenar > a 12 segun nacionalidad
// si son iguales segun edad de menor a mayor ------> MENOS SIGNIFICATIVA

func OrdenarFila(arr []persona) []persona {
	maxEdad, cantMenores := 0, 0
	for i := 0; i < len(arr); i++ {
		if arr[i].Edad() > maxEdad {
			maxEdad = arr[i].Edad()
		}
		if arr[i].Edad() < 12 {
			cantMenores += 1
		}
	}
	// ordeno segun edad 
	arr = CountingSort(arr, maxEdad+1, "edad")
	menores := arr[:cantMenores+1]
	mayores := arr[cantMenores+1:]
	// ordeno mayores segun nacionalidad
	mayores = CountingSort(mayores, 33, "nacionalidad")
	// uno todo con append que es O(n)
	res := append(menores, mayores...)
	return res
}

func CountingSort(arr []persona, k int, criterio string) []persona {
	count := make([]int, k)
	res := make([]persona, len(arr))

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

func pos(i persona, criterio string) int {
	if criterio == "edad" {
		return i.Edad()
	} else {
		return i.Nacionalidad()
	}
}

func main() {
	arr := []persona{CrearPersona(3, 5), CrearPersona(45, 9),CrearPersona(67, 1), CrearPersona(32, 9), CrearPersona(12, 7), CrearPersona(11, 1), CrearPersona(10, 1), CrearPersona(32, 17), CrearPersona(45, 13), CrearPersona(7, 9), CrearPersona(56, 23), CrearPersona(45, 31), CrearPersona(9, 21)}
	fmt.Println(OrdenarFila(arr))
}