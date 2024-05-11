package cola_prioridad_test

import (
	"github.com/stretchr/testify/require"
	TDAHeap "tdas/cola_prioridad"
	"testing"
)

func cmpIntMax(n1, n2 int) int {
	// tienen prioridad los int mayores
	if n1 > n2 {
		return 1
	}
	if n2 > n1 {
		return -1
	}
	return 0
}

func cmpIntMin(n1, n2 int) int {
	// tienen prioridad los int menores
	if n1 < n2 {
		return 1
	}
	if n2 < n1 {
		return -1
	}
	return 0
}

func cmpLenString(s1, s2 string) int {
	// tienen prioridad los strings mas cortos
	if len(s1) < len(s2) {
		return 1
	}
	if len(s2) < len(s1) {
		return -1
	}
	return 0
}

func cmpIntDivPorDos(n1, n2 int) int {
	// tienen prioridad los divisibles por dos
	if n1%2 == 0 && n2%2 != 0 {
		return 1
	}
	if n2%2 == 0 && n1%2 != 0 {
		return -1
	}
	return 0
}

func TestHeapCumplePrioridad(t *testing.T) {
	arregloInt := []int{5, 12, 8, 23, 1, 9, 6} // no se tiene por que modificar el arreglo que recibe CrearHeap

	arregloString := []string{"aaa", "aa", "abcc", "aaccc", "bbca", "aaaaaa", "aaab", "bb"}

	heapIntsMax := TDAHeap.CrearHeapArr[int](arregloInt, cmpIntMax)            // [23,12,9,5,1,8,6]
	heapIntsMin := TDAHeap.CrearHeapArr[int](arregloInt, cmpIntMin)            // [1,5,6,23,12,9,8]
	heapIntsDiv := TDAHeap.CrearHeapArr[int](arregloInt, cmpIntDivPorDos)      // [12,5,8,23,1,9,6]
	heapStringLen := TDAHeap.CrearHeapArr[string](arregloString, cmpLenString) // [aa,bb,abcc,aaa,bbca,aaaaaa,aaab,aaccc]

	require.EqualValues(t, len(arregloInt), heapIntsMax.Cantidad())
	require.EqualValues(t, len(arregloInt), heapIntsMin.Cantidad())
	require.EqualValues(t, len(arregloInt), heapIntsDiv.Cantidad())
	require.EqualValues(t, len(arregloString), heapStringLen.Cantidad())
	require.EqualValues(t, heapIntsMax.VerMax(), heapIntsMax.Desencolar())
	require.EqualValues(t, heapIntsMin.VerMax(), heapIntsMin.Desencolar())
	require.EqualValues(t, heapIntsDiv.VerMax(), heapIntsDiv.Desencolar())
	require.EqualValues(t, heapStringLen.VerMax(), heapStringLen.Desencolar())

	require.EqualValues(t, len(arregloInt)-1, heapIntsMax.Cantidad())
	require.EqualValues(t, len(arregloInt)-1, heapIntsMin.Cantidad())
	require.EqualValues(t, len(arregloInt)-1, heapIntsDiv.Cantidad())
	require.EqualValues(t, len(arregloString)-1, heapStringLen.Cantidad())

	heapIntsMax.Encolar(234)
	require.EqualValues(t, 234, heapIntsMax.VerMax())
	heapIntsMin.Encolar(-1)
	require.EqualValues(t, -1, heapIntsMin.VerMax())
	heapIntsDiv.Encolar(2)
	require.EqualValues(t, 6, heapIntsDiv.VerMax())
	heapStringLen.Encolar("a")
	require.EqualValues(t, "a", heapStringLen.VerMax())

	require.EqualValues(t, len(arregloInt), heapIntsMax.Cantidad())
	require.EqualValues(t, len(arregloInt), heapIntsMin.Cantidad())
	require.EqualValues(t, len(arregloInt), heapIntsDiv.Cantidad())
	require.EqualValues(t, len(arregloString), heapStringLen.Cantidad())
}

func TestCrearHeap(t *testing.T) {
	heapVacio := TDAHeap.CrearHeap[int](cmpIntMin)
	require.True(t, heapVacio.EstaVacia())
	require.EqualValues(t, 0, heapVacio.Cantidad())

	heapVacio.Encolar(1)
	heapVacio.Encolar(-1)

	require.False(t, heapVacio.EstaVacia())
	require.EqualValues(t, 2, heapVacio.Cantidad())
	require.EqualValues(t, -1, heapVacio.VerMax())
}

func TestCrearHeapArr(t *testing.T) {
	arreglo := []string{"bc", "abcd", "bcb", "aaaaa", "abb"}
	heapArr := TDAHeap.CrearHeapArr[string](arreglo, cmpLenString)
	require.False(t, heapArr.EstaVacia())
	require.EqualValues(t, len(arreglo), heapArr.Cantidad())
	heapArr.Encolar("a")
	require.EqualValues(t, "a", heapArr.VerMax())
	require.EqualValues(t, len(arreglo)+1, heapArr.Cantidad())
}

func TestHeapVacio(t *testing.T) {
	heapVacio := TDAHeap.CrearHeap[int](cmpIntMax)
	require.PanicsWithValue(t, "La cola esta vacia", func() { heapVacio.VerMax() })
	require.PanicsWithValue(t, "La cola esta vacia", func() { heapVacio.Desencolar() })
	require.True(t, heapVacio.EstaVacia())
}

func TestEncolarDesencolar(t *testing.T) {
	heapVacio := TDAHeap.CrearHeap[int](cmpIntMax)
	heapVacio.Encolar(2)
	heapVacio.Encolar(5)
	heapVacio.Encolar(1)
	heapVacio.Encolar(8)
	require.EqualValues(t, 8, heapVacio.VerMax())
	heapVacio.Encolar(7)
	heapVacio.Encolar(-1)

	heapVacio.Desencolar()
	require.EqualValues(t, 7, heapVacio.VerMax())
	heapVacio.Desencolar()
	heapVacio.Desencolar()
	heapVacio.Desencolar()
	require.EqualValues(t, 1, heapVacio.VerMax())
	heapVacio.Desencolar()
	require.EqualValues(t, -1, heapVacio.VerMax())
	heapVacio.Desencolar()
	require.True(t, heapVacio.EstaVacia())
}

func TestVolumen(t *testing.T) {
	heapMax := TDAHeap.CrearHeap[int](cmpIntMax)
	heapMin := TDAHeap.CrearHeap[int](cmpIntMin)
	for i := 1; i <= 10000; i++ {
		heapMax.Encolar(i)
		heapMin.Encolar(i)
		require.EqualValues(t, i, heapMax.VerMax())
		require.EqualValues(t, 1, heapMin.VerMax())
	}
	for i := 10000; i > 0; i-- {
		require.EqualValues(t, i, heapMax.VerMax())
		require.EqualValues(t, i, heapMax.Desencolar())
		require.EqualValues(t, 10000-i+1, heapMin.VerMax())
		require.EqualValues(t, 10000-i+1, heapMin.Desencolar())
	}
}

func TestHeapSort(t *testing.T) {
	arregloInts1 := []int{5, 3, 36, 3, 2, 5, 76, 1, 90, -1}
	arregloInts2 := make([]int, len(arregloInts1))
	copy(arregloInts2, arregloInts1)
	arregloStrings := []string{"abc", "ac", "abc", "aa", "bacab", "a", "bbca"}

	TDAHeap.HeapSort[int](arregloInts1, cmpIntMax)
	TDAHeap.HeapSort[int](arregloInts2, cmpIntMin)
	TDAHeap.HeapSort[string](arregloStrings, cmpLenString)

	arregloIntsEsperado1 := []int{-1, 1, 2, 3, 3, 5, 5, 36, 76, 90}
	arregloIntsEsperado2 := []int{90, 76, 36, 5, 5, 3, 3, 2, 1, -1}
	arregloStringsEsperado := []string{"bacab", "bbca", "abc", "abc", "aa", "ac", "a"}

	require.EqualValues(t, arregloIntsEsperado1, arregloInts1)
	require.EqualValues(t, arregloIntsEsperado2, arregloInts2)
	require.EqualValues(t, arregloStringsEsperado, arregloStrings)
}
