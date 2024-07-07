// primitiva de listaEnlazada
// no se pueden usar estructuras auxiliares

func (lista listaEnlazada[T]) AnteKUltimo(k int) T {
	// creo un puntero al primer elemento
	// lo avanzo k veces
	// creo un segundo puntero al primero
	// avanzo ambos punteros hasta que el primero llegue al final
	// devuelve el dato del segundo puntero
}


Consideraciones TDA Lista 

type listaEnlazada[T any] struct {
	primero *nodoLista[T]
	ultimo *nodoLista[T]
	largo int
}

type Lista[T any] interface {

}