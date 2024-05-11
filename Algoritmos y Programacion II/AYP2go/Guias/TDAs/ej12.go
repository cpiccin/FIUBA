package main



func FiltrarCola[K any](cola Cola[K], filtro func(K) bool) {
	aux := CrearColaEnlazada[K]()
	for ! cola.EstaVacia() {
		elem := cola.VerPrimero()
		if ! filtro(elem) {
			cola.Desencolar()
		} else {
			aux.Encolar(cola.Desencolar())
		}
	}
	for ! aux.EstaVacia() {
		cola.Encolar(aux.Desencolar())
	}
}