package cola

// import "fmt"

type nodoCola[T any] struct {
	dato T
	prox *nodoCola[T]
}

func crearNodo[T any](dato T) *nodoCola[T] {
	nuevo_nodo := new(nodoCola[T])
	nuevo_nodo.dato = dato
	return nuevo_nodo
}

// --------------------------------------------------- //

type colaEnlazada[T any] struct {
	primero *nodoCola[T]
	ultimo  *nodoCola[T]
}

func CrearColaEnlazada[T any]() Cola[T] {
	nueva_cola := new(colaEnlazada[T])
	return nueva_cola
}

func (cola *colaEnlazada[T]) EstaVacia() bool {
	return cola.primero == nil
}

func (cola *colaEnlazada[T]) VerPrimero() T {
	cola.verificaExcepcion()
	return cola.primero.dato
}

func (cola *colaEnlazada[T]) Encolar(dato T) {
	if cola.EstaVacia() {
		cola.primero = crearNodo[T](dato)
		cola.ultimo = cola.primero
	} else {
		cola.ultimo.prox = crearNodo[T](dato)
		cola.ultimo = cola.ultimo.prox
	}
}

func (cola *colaEnlazada[T]) Desencolar() T {
	cola.verificaExcepcion()
	dato_desencolado := cola.primero.dato
	cola.primero = cola.primero.prox
	return dato_desencolado
}

func (cola *colaEnlazada[T]) verificaExcepcion() {
	if cola.EstaVacia() {
		panic("La cola esta vacia")
	}
}

func (cola *colaEnlazada[T]) Multiprimeros(k int) []T {
    
	aux := new(colaEnlazada[T])
	slice_final := make([]T, k)
	n := k
	
	for !cola.EstaVacia() {
		if n > 0 {
			slice_final[k-n] = cola.VerPrimero()
		}
		aux.Encolar(cola.Desencolar())
		n--
		}
	
	if len(slice_final) > (k-n) {
		slice_final = slice_final[:k-n]
	}

	for !aux.EstaVacia() {
		cola.Encolar(aux.Desencolar())
	}

	return slice_final
}