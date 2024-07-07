// Implementar una función func FiltrarCola[K any](cola Cola[K], filtro func(K) bool) , que elimine los elementos encolados
// para los cuales la función filtro devuelve false. Aquellos elementos que no son eliminados deben permanecer en el mismo 
// orden en el que estaban antes de invocar a la función. No es necesario destruir los elementos que sí fueron eliminados. 
// Se pueden utilizar las estructuras auxiliares que se consideren necesarias y no está permitido acceder a la estructura 
// interna de la cola (es una función). ¿Cuál es el orden del algoritmo implementado?



func FiltrarCola[K any](cola Cola[K], filtro func(K) bool) {
	colaAux := CrearColaEnlazada[K]()
	for ! cola.EstaVacia() {
		elem := cola.Desencolar()
		if filtro(elem) {
			colaAux.Encolar(elem)
		}
	}
	for ! colaAux.EstaVacia() {
		cola.Encolar(colaAux.Desencolar())
	}
}