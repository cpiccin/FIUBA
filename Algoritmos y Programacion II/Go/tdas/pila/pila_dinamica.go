package pila

/* Definición del struct pila proporcionado por la cátedra. */

type pilaDinamica[T any] struct {
	datos    []T
	cantidad int
}

func CrearPilaDinamica[T any]() Pila[T] {
	pila := new(pilaDinamica[T])
	pila.datos, pila.cantidad = make([]T, 10), 0
	return pila
}

func (pila *pilaDinamica[T]) Apilar(elem T) {
	// Agrega un elemento a la pila.

	if pila.cantidad == cap(pila.datos) {
		pila.redimensionar(pila.cantidad * 2)
	}

	pila.datos[pila.cantidad] = elem
	pila.cantidad++
}

func (pila *pilaDinamica[T]) Desapilar() T {
	// Desapila el ultimo elemento de la pila y lo devuelve. Levanta un panic si esta vacia (no se puede desapilar nada).
	pila.verificaExcepcion()

	if (pila.cantidad)*4 <= cap(pila.datos) {
		pila.redimensionar(cap(pila.datos) / 2)
	}

	pila.cantidad--
	return (pila.datos)[pila.cantidad]
}

func (pila *pilaDinamica[T]) EstaVacia() bool {
	// Devuelve true si la pila esta vacia.
	return pila.cantidad == 0
}

func (pila *pilaDinamica[T]) VerTope() T {
	// Muestra el tope de la pila y lo devuelve. Levanta un panic si esta vacia (no hay ningun tope que ver).
	pila.verificaExcepcion()
	return (pila.datos)[pila.cantidad-1]
}

func (pila *pilaDinamica[T]) redimensionar(nueva_cap int) {
	nueva_pila := new(pilaDinamica[T])
	nueva_pila.datos = make([]T, nueva_cap)
	copy(nueva_pila.datos, pila.datos)
	pila.datos = nueva_pila.datos
}

func (pila *pilaDinamica[T]) verificaExcepcion() {
	// Si se intenta desapilar o ver tope cuando la pila esta vacia levanta un panic.
	if pila.EstaVacia() {
		panic("La pila esta vacia")
	}
}
