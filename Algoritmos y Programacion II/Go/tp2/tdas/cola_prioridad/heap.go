package cola_prioridad

const (
	TAM_INICIAL                = 15
	FACTOR_LIMITE_PARA_REDUCIR = 4
	FACTOR_REDIMENSION         = 2
)

type heap[T any] struct {
	arr      []T
	cantidad int
	funcCmp  func(T, T) int
}

func CrearHeap[T any](funcionCmp func(T, T) int) ColaPrioridad[T] {
	nuevo := new(heap[T])
	nuevo.arr, nuevo.cantidad, nuevo.funcCmp = make([]T, TAM_INICIAL), 0, funcionCmp
	return nuevo
}

func CrearHeapArr[T any](arreglo []T, funcionCmp func(T, T) int) ColaPrioridad[T] {
	if len(arreglo) == 0 {
		return CrearHeap[T](funcionCmp)
	}
	nuevo := new(heap[T])
	nuevo.arr, nuevo.cantidad, nuevo.funcCmp = make([]T, len(arreglo)), len(arreglo), funcionCmp
	copy(nuevo.arr, arreglo)
	heapify(nuevo.arr, funcionCmp)
	return nuevo
}

func (h *heap[T]) EstaVacia() bool {
	return h.cantidad == 0
}

func (h *heap[T]) VerMax() T {
	h.verificaColaVacia()
	return h.arr[0]
}

func (h *heap[T]) Cantidad() int {
	return h.cantidad
}

func (h *heap[T]) Desencolar() T {
	h.verificaColaVacia()
	h.cantidad--
	swap(h.arr, 0, h.cantidad)
	downHeap(h.Cantidad(), 0, h.arr, h.funcCmp)
	h.redimensionarSiEsNecesario()
	return h.arr[h.cantidad]
}

func (h *heap[T]) Encolar(dato T) {
	h.redimensionarSiEsNecesario()
	h.arr[h.cantidad] = dato
	upHeap(h.cantidad, h.arr, h.funcCmp)
	h.cantidad++
}

func HeapSort[T any](elementos []T, funcionCmp func(T, T) int) {
	heapify(elementos, funcionCmp)
	cantidad := len(elementos)
	for i := len(elementos) - 1; i >= 0; i-- {
		cantidad--
		swap(elementos, 0, i)
		downHeap(cantidad, 0, elementos, funcionCmp)
	}
}

func heapify[T any](arr []T, funcionCmp func(T, T) int) {
	for i := (len(arr) - 1) / 2; i >= 0; i-- {
		downHeap(len(arr), i, arr, funcionCmp)
	}
}

func downHeap[T any](cantidad, pos int, arr []T, funcionCmp func(T, T) int) {
	posPadre := pos
	posHijoIzq := 2*pos + 1
	posHijoDer := 2*pos + 2

	if posHijoIzq < cantidad && funcionCmp(arr[posHijoIzq], arr[posPadre]) > 0 { //izq > que posPadre
		posPadre = posHijoIzq
	}
	if posHijoDer < cantidad && funcionCmp(arr[posHijoDer], arr[posPadre]) > 0 { //der > que posPadre
		posPadre = posHijoDer
	}

	if posPadre != pos { // alguno de los hijos era mayor
		swap(arr, pos, posPadre)
		downHeap(cantidad-1, posPadre, arr, funcionCmp)
	}
	return
}

func upHeap[T any](pos int, arr []T, funcionCmp func(T, T) int) {
	if pos == 0 { // si se llego a la raiz
		return
	}

	posPadre := (pos - 1) / 2

	if funcionCmp(arr[pos], arr[posPadre]) > 0 {
		swap(arr, pos, posPadre)
		upHeap(posPadre, arr, funcionCmp)
	}
}

func (h *heap[T]) redimensionarSiEsNecesario() {
	if h.cantidad == 0 {
		return
	}
	if (h.cantidad * FACTOR_LIMITE_PARA_REDUCIR) < len(h.arr) {
		h.redimensionar(len(h.arr) / FACTOR_REDIMENSION)
	} else if h.cantidad == len(h.arr) {
		h.redimensionar(len(h.arr) * FACTOR_REDIMENSION)
	}
}

func (h *heap[T]) redimensionar(nuevaCap int) {
	nuevoHeap := new(heap[T])
	nuevoHeap.arr = make([]T, nuevaCap)
	copy(nuevoHeap.arr, h.arr)
	h.arr = nuevoHeap.arr
}

func swap[T any](arr []T, i, j int) {
	arr[i], arr[j] = arr[j], arr[i]
}

func (h *heap[T]) verificaColaVacia() {
	if h.EstaVacia() {
		panic("La cola esta vacia")
	}
}
