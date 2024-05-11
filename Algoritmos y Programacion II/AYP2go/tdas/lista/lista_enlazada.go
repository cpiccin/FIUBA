package lista

type nodoLista[T any] struct {
	dato T
	prox *nodoLista[T]
}

func crearNodo[T any](dato T) *nodoLista[T] {
	return &nodoLista[T]{dato: dato}
}

type listaEnlazada[T any] struct {
	primero *nodoLista[T]
	ultimo  *nodoLista[T]
	largo   int
}

func CrearListaEnlazada[T any]() Lista[T] {
	return new(listaEnlazada[T])
}

func (lista *listaEnlazada[T]) EstaVacia() bool {
	return lista.largo == 0
}

func (lista *listaEnlazada[T]) VerPrimero() T {
	lista.verificaExcepcion()
	return lista.primero.dato
}

func (lista *listaEnlazada[T]) VerUltimo() T {
	lista.verificaExcepcion()
	return lista.ultimo.dato
}

func (lista *listaEnlazada[T]) Largo() int {
	return lista.largo
}

func (lista *listaEnlazada[T]) InsertarPrimero(dato T) {
	nuevoPrimero := crearNodo[T](dato)
	nuevoPrimero.prox = lista.primero
	if lista.EstaVacia() { // si la lista esta vacia el nodo es el primero y el ultimo
		lista.ultimo = nuevoPrimero
	}
	lista.largo++
	lista.primero = nuevoPrimero
}

func (lista *listaEnlazada[T]) InsertarUltimo(dato T) {
	nuevoUltimo := crearNodo[T](dato)
	if lista.EstaVacia() { // si la lista esta vacia, insertar al final es insertar al principio
		lista.primero = nuevoUltimo
	} else {
		lista.ultimo.prox = nuevoUltimo
	}
	lista.largo++
	lista.ultimo = nuevoUltimo
}

func (lista *listaEnlazada[T]) BorrarPrimero() T {
	lista.verificaExcepcion()
	elemBorrado := lista.primero
	lista.largo--
	if lista.EstaVacia() {
		lista.ultimo = lista.primero.prox
	}
	lista.primero = lista.primero.prox
	return elemBorrado.dato
}

func (lista listaEnlazada[T]) Iterar(visitar func(T) bool) {
	actual := lista.primero
	for i := 0; i < lista.largo; i++ {
		if visitar(actual.dato) {
			actual = actual.prox
		} else {
			break
		}
	}
}

func (lista *listaEnlazada[T]) verificaExcepcion() {
	if lista.EstaVacia() {
		panic("La lista esta vacia")
	}
}

// ----------------------------------------------- //

type iteradorLista[T any] struct {
	actual   *nodoLista[T]
	anterior *nodoLista[T]
	l        *listaEnlazada[T]
}

func (lista *listaEnlazada[T]) Iterador() IteradorLista[T] {
	nuevoIter := new(iteradorLista[T])
	nuevoIter.l = lista
	nuevoIter.actual = lista.primero
	return nuevoIter
}

func (iter *iteradorLista[T]) VerActual() T {
	iter.verificaFinDeIteracion()
	return iter.actual.dato
}

func (iter *iteradorLista[T]) HaySiguiente() bool {
	return iter.actual != nil
}

func (iter *iteradorLista[T]) Siguiente() {
	iter.verificaFinDeIteracion()
	iter.anterior = iter.actual
	iter.actual = iter.actual.prox
}

func (iter *iteradorLista[T]) Insertar(dato T) {
	nuevoElemento := crearNodo[T](dato)
	if !iter.HaySiguiente() { // lista vacia o esta en al final de la lista
		iter.l.ultimo = nuevoElemento
	}
	if iter.anterior == nil { // es la posicion inicial
		iter.l.primero = nuevoElemento
	} else {
		iter.anterior.prox = nuevoElemento
	}
	nuevoElemento.prox = iter.actual
	iter.actual = nuevoElemento
	iter.l.largo++
}

func (iter *iteradorLista[T]) Borrar() T {
	iter.verificaFinDeIteracion()
	borrado := iter.actual
	if iter.actual.prox == nil {
		iter.l.ultimo = iter.anterior
	}
	if iter.anterior == nil {
		iter.l.primero = iter.actual.prox
	} else {
		iter.anterior.prox = iter.actual.prox
	}
	iter.actual = iter.actual.prox
	iter.l.largo--
	return borrado.dato
}

func (iter *iteradorLista[T]) verificaFinDeIteracion() {
	if !iter.HaySiguiente() {
		panic("El iterador termino de iterar")
	}
}
