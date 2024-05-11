package main 

import(
	"fmt"
	TDAPila "TDAs/pila"
)

func main(){
	pila1 := TDAPila.CrearPilaDinamica[int]()
	pila2 := TDAPila.CrearPilaDinamica[int]()

	pila1.Apilar(5)
	pila1.Apilar(3)
	pila1.Apilar(2)
	pila1.Apilar(2)
	pila1.Apilar(1)

	pila2.Apilar(7)
	pila2.Apilar(5)
	pila2.Apilar(4)
	pila2.Apilar(2)

	slice := MergePilas(pila1, pila2)
	fmt.Println(slice)
}

// dadas 2 pilas de enteros positivos (por ahi valores repetidos) con elementos ingresados
// de menor a mayor [2,3,5,6,6,8,23]
// implementar una funcion que DEVUELVA	un array ordenado de mayor a menor con valores
// de ambas pilas sin repetir

func MergePilas(pila1, pila2 TDAPila.Pila[int]) []int {
	var slice_final []int
	
	for ! pila1.EstaVacia() && ! pila2.EstaVacia() { // mientras que ninguna este vacia
		var actual int
		if pila1.VerTope() < pila2.VerTope() {
			actual = pila1.Desapilar()
		} else {
			actual = pila2.Desapilar()
		}
		if len(slice_final) == 0 || slice_final[len(slice_final)-1] != actual {
			slice_final = append(slice_final, actual)
		} 
	}
	for ! pila1.EstaVacia() {
		actual := pila1.Desapilar()
		if len(slice_final) == 0 || slice_final[len(slice_final)-1] != actual {
			slice_final = append(slice_final, actual)
		} 
	}
	for ! pila2.EstaVacia() {
		actual := pila2.Desapilar()
		if len(slice_final) == 0 || slice_final[len(slice_final)-1] != actual  {
			slice_final = append(slice_final, actual)
	}
}

	return slice_final
}