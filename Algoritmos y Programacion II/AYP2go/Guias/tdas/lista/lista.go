package lista

type Lista[T any] interface {
	// Devuelve true si la lista esta vacia, false en caso contrario.
	EstaVacia() bool
	// Inserta un nuevo elemento al principio de la lista.
	InsertarPrimero(T)
	// Inserta un nuevo elemento al final de la lista.
	InsertarUltimo(T)
	// Borra el primer elemento de la lista y lo devuelve. Levanta un panic si esta vacia.
	BorrarPrimero() T
	// Devuelve el primer elemento de la lista. Levanta un panic si esta vacia.
	VerPrimero() T
	// Devuelve el ultimo elemento de la lista. Levanta un panic si esta vacia.
	VerUltimo() T
	// Devuelve el largo, la cantidad de elementos de la lista.
	Largo() int
	// Itera sobre cada elemento de la lista y aplica la funcion visitar sobre cada uno
	// hasta que esta devuelva false o termine de recorrerse la lista.
	Iterar(visitar func(T) bool)
	// Inicializa un iterador que permite recorrer la lista.
	Iterador() IteradorLista[T]
}

type IteradorLista[T any] interface {
	// Devuelve el elemento actual sobre el que se esta en la iteracion.
	// Levanta un panic si no hay mas elementos que iterar.
	VerActual() T
	// Devuelve true si el elemento actual sigue siendo parte la lista. False si no hay nada que iterar
	HaySiguiente() bool
	// Avanza al siguiente elemento de la lista. Levanta un panic si no hay que iterar.
	Siguiente()
	// Inserta un elemento en la posicion del elemento actual.
	Insertar(T)
	// Borra el elemento de la posicion actual. Levanta un panic si no hay nada que borrar.
	Borrar() T
}
