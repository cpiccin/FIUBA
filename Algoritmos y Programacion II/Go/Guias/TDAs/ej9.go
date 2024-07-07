// (ej10 en RPL)

// Implementar en Go una primitiva func (lista *ListaEnlazada) Invertir() que invierta la lista, 
// sin utilizar estructuras auxiliares. 
// Indicar y justificar el orden de la primitiva.


func (lista *listaEnlazada[T]) Invertir() {
	var ant *nodoLista[T]
	var sig *nodoLista[T]
	act := lista.primero
	
    for act != nil {
		sig = act.siguiente
		act.siguiente = ant 
		ant = act 
		act = sig
	}
	lista.primero = ant
}

