// Cambiar prioridad

func (heap *heap[T]) CambiarPrioridad(nuevaPrioridad func(a, b T) int) {
	heap.cmp = nuevaPrioridad
	heapify(heap.datos, heap.cantidad, nuevaPrioridad)
}