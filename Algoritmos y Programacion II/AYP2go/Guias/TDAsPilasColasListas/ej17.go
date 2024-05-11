// Escribir una primitiva para la pila (dinámica) cuya firma es func (pila pilaDinamica[T]) Transformar(aplicar func(T) T) Pila[T] que
// devuelva una nueva pila cuyos elementos sean los resultantes de aplicarle la función aplicar a cada elemento de la pila original. 
// Los elementos en la nueva pila deben tener el orden que tenían en la pila original, y la pila original debe quedar en el mismo estado 
// al inicial. Indicar y justificar la complejidad de la primitiva.

// Por ejemplo, para la pila de enteros [ 1, 2, 3, 6, 2 ] (tope es el número 2), y la función sumarUno (que devuelve la suma entre el número
// 1 y el número recibido), la pila resultante debe ser [ 2, 3, 4, 7, 3 ] (el tope es el número 3).


func (pila *pilaDinamica[T]) Transformar(aplicar func(T) T) Pila[T] {
	pilaAux := CrearPilaDinamica[T]() 
	pilaRes := CrearPilaDinamica[T]()
	for ! pila.EstaVacia() {
		pilaAux.Apilar(pila.Desapilar())
	}
	for ! pilaAux.EstaVacia() {
		elem := pilaAux.Desapilar()
		pilaRes.Apilar(aplicar(elem))
		pila.Apilar(elem)
	}
	return pilaRes
}

func (pila *pilaDinamica[T]) Transformar(aplicar func(T) T) Pila[T] {
	pilaRes := CrearPilaDinamica[T]()
	for i := 0; i < pila.cantidad; i++ {
		pilaRes.Apilar(aplicar(pila.datos[i]))
	}
	return pilaRes
}