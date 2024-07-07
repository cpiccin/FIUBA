package lista_test

import (
	"github.com/stretchr/testify/require"
	TDALista "tdas/lista"
	"testing"
)

// -- Test comportamiento de lista enlazada

func TestListaVacia(t *testing.T) {

	lista := TDALista.CrearListaEnlazada[int]()

	require.NotNil(t, lista)
	require.True(t, lista.EstaVacia())
	require.EqualValues(t, 0, lista.Largo())
	require.PanicsWithValue(t, "La lista esta vacia", func() { lista.VerPrimero() })
	require.PanicsWithValue(t, "La lista esta vacia", func() { lista.VerUltimo() })

}

func TestInsertarPrimeroUltimo(t *testing.T) {

	lista := TDALista.CrearListaEnlazada[int]()

	require.True(t, lista.EstaVacia())

	lista.InsertarPrimero(1)
	require.False(t, lista.EstaVacia())
	// como es una lista vacia el primero y ultimo son iguales
	require.EqualValues(t, 1, lista.VerPrimero())
	require.EqualValues(t, 1, lista.VerUltimo())

	lista.InsertarPrimero(2)
	require.EqualValues(t, 2, lista.VerPrimero())
	require.EqualValues(t, 1, lista.VerUltimo())
	lista.InsertarPrimero(3)
	require.EqualValues(t, 3, lista.VerPrimero())
	require.EqualValues(t, 1, lista.VerUltimo())
	require.EqualValues(t, 3, lista.Largo())
	// lista = [3,2,1]
	lista.InsertarUltimo(5)
	lista.InsertarUltimo(6)
	// lista = [3,2,1,5,6]
	require.EqualValues(t, 3, lista.VerPrimero())
	require.EqualValues(t, 6, lista.VerUltimo())
	require.EqualValues(t, 5, lista.Largo())

	lista = TDALista.CrearListaEnlazada[int]()
	lista.InsertarUltimo(1)
	lista.InsertarPrimero(3)
	lista.InsertarUltimo(2)
	lista.InsertarPrimero(5)
	// lista = [5,3,1,2]
	require.EqualValues(t, 5, lista.VerPrimero())
	require.EqualValues(t, 2, lista.VerUltimo())

}

func TestBorrarPrimero(t *testing.T) {
	lista := TDALista.CrearListaEnlazada[int]()

	lista.InsertarPrimero(1)
	require.False(t, lista.EstaVacia())
	require.EqualValues(t, 1, lista.BorrarPrimero())
	require.True(t, lista.EstaVacia())

	lista.InsertarUltimo(3)
	require.False(t, lista.EstaVacia())
	require.EqualValues(t, 3, lista.BorrarPrimero())
	require.True(t, lista.EstaVacia())

	lista.InsertarUltimo(1)
	lista.InsertarUltimo(2)
	lista.InsertarUltimo(3)

	require.EqualValues(t, 3, lista.Largo())
	require.EqualValues(t, 1, lista.VerPrimero())
	require.EqualValues(t, 1, lista.BorrarPrimero())
	// [1,2,3] --borrar primero--> [2,3]
	require.EqualValues(t, 2, lista.VerPrimero())
	require.EqualValues(t, 3, lista.VerUltimo())
	require.EqualValues(t, 2, lista.Largo())

}

func TestVerPrimeroUltimo(t *testing.T) {
	lista := TDALista.CrearListaEnlazada[string]()

	lista.InsertarUltimo("Aruba")
	require.EqualValues(t, "Aruba", lista.VerPrimero())
	require.EqualValues(t, "Aruba", lista.VerUltimo())
	lista.InsertarUltimo("Fiji")
	lista.InsertarUltimo("Libano")
	lista.InsertarUltimo("Canada")
	require.EqualValues(t, "Aruba", lista.VerPrimero())
	require.EqualValues(t, "Canada", lista.VerUltimo())
	// lista = ["Aruba","Fiji","Libano","Canada"]
	lista.BorrarPrimero()
	lista.BorrarPrimero()
	// lista = ["Libano","Canada"]
	require.EqualValues(t, "Libano", lista.VerPrimero())
	require.EqualValues(t, "Canada", lista.VerUltimo())
	lista.BorrarPrimero()
	// lista = ["Canada"]
	require.EqualValues(t, "Canada", lista.VerPrimero())
	require.EqualValues(t, lista.VerPrimero(), lista.VerUltimo())
	lista.BorrarPrimero()
	//lista = []
	require.PanicsWithValue(t, "La lista esta vacia", func() { lista.VerPrimero() })
	require.PanicsWithValue(t, "La lista esta vacia", func() { lista.VerUltimo() })

}

func TestVolumen(t *testing.T) {
	lista := TDALista.CrearListaEnlazada[int]()
	tam := 10000

	for i := 0; i < tam; i++ {
		lista.InsertarUltimo(i + 1)
		require.EqualValues(t, i+1, lista.VerUltimo())
		require.EqualValues(t, i+1, lista.Largo())
	}
	require.EqualValues(t, 1, lista.VerPrimero())
	require.EqualValues(t, tam, lista.VerUltimo())
	require.EqualValues(t, tam, lista.Largo())

	for i := 0; i < tam-1; i++ {
		require.EqualValues(t, i+1, lista.VerPrimero())
		require.EqualValues(t, i+1, lista.BorrarPrimero())
	}

	require.EqualValues(t, tam, lista.VerPrimero())
	require.EqualValues(t, tam, lista.VerUltimo())
	require.EqualValues(t, 1, lista.Largo())
	require.EqualValues(t, tam, lista.BorrarPrimero())
	require.True(t, lista.EstaVacia())

}

func TestPruebaInsertarYBorrarVarios(t *testing.T) {
	lista := TDALista.CrearListaEnlazada[int]()

	for i := 0; i < 20; i++ {
		lista.InsertarUltimo(i + 1)
	}
	require.EqualValues(t, 1, lista.VerPrimero())
	require.EqualValues(t, 20, lista.VerUltimo())
	require.EqualValues(t, 20, lista.Largo())

	for i := 20; i < 50; i++ {
		lista.InsertarUltimo(i + 1)
	}
	require.EqualValues(t, 1, lista.VerPrimero())
	require.EqualValues(t, 50, lista.VerUltimo())
	require.EqualValues(t, 50, lista.Largo())

	lista.InsertarUltimo(234)
	require.EqualValues(t, 1, lista.VerPrimero())
	require.EqualValues(t, 234, lista.VerUltimo())
	require.EqualValues(t, 51, lista.Largo())

	for i := 0; i < 50; i++ {
		require.EqualValues(t, i+1, lista.BorrarPrimero())
	}
	require.EqualValues(t, 234, lista.VerPrimero())
	require.EqualValues(t, 234, lista.VerUltimo())
	require.EqualValues(t, 1, lista.Largo())

	lista.BorrarPrimero()
	require.PanicsWithValue(t, "La lista esta vacia", func() { lista.VerPrimero() })
	require.PanicsWithValue(t, "La lista esta vacia", func() { lista.VerUltimo() })
	require.True(t, lista.EstaVacia())

}

func TestSeComportaComoNueva(t *testing.T) {
	lista := TDALista.CrearListaEnlazada[int]()

	lista.InsertarUltimo(1)
	lista.InsertarUltimo(2)
	lista.InsertarUltimo(3)
	lista.BorrarPrimero()
	lista.BorrarPrimero()
	lista.BorrarPrimero()

	require.True(t, lista.EstaVacia())
	require.PanicsWithValue(t, "La lista esta vacia", func() { lista.VerPrimero() })
	require.PanicsWithValue(t, "La lista esta vacia", func() { lista.VerUltimo() })
	require.PanicsWithValue(t, "La lista esta vacia", func() { lista.BorrarPrimero() })

	lista.InsertarUltimo(4)
	require.False(t, lista.EstaVacia())
	require.EqualValues(t, 4, lista.VerPrimero())
	require.EqualValues(t, 4, lista.VerUltimo())

}

// --Test iterador interno

func TestUsoVisitar(t *testing.T) {
	lista := TDALista.CrearListaEnlazada[int]()
	suma, cont := 0, 0
	sumaPtr, contPtr := &suma, &cont

	lista.InsertarUltimo(1)
	lista.InsertarUltimo(2)
	lista.InsertarUltimo(3)
	lista.InsertarUltimo(4)
	lista.InsertarUltimo(5)
	lista.InsertarUltimo(6)

	// cuenta cuantos elementos hay en la lista
	lista.Iterar(func(i int) bool {
		*contPtr += 1
		return true
	})

	require.EqualValues(t, cont, lista.Largo())

	// suma todos los elementos de la lista
	lista.Iterar(func(i int) bool {
		*sumaPtr += i
		return true
	})

	require.EqualValues(t, 21, suma)

}

func TestIteracionCompleta(t *testing.T) {
	lista := TDALista.CrearListaEnlazada[int]()
	lista.InsertarUltimo(1)
	lista.InsertarUltimo(2)
	lista.InsertarUltimo(3)
	lista.InsertarUltimo(4)
	lista.InsertarUltimo(5)
	lista.InsertarUltimo(6)
	n := 0
	nPtr := &n

	// itero hasta que n sea el largo de la lista o sea la recorrio completa
	lista.Iterar(func(i int) bool {
		*nPtr += 1
		return n <= lista.Largo()
	})

	require.EqualValues(t, lista.Largo(), n)

}

func TestIteracionConCorte(t *testing.T) {
	lista := TDALista.CrearListaEnlazada[string]()
	lista.InsertarUltimo("Arabia")
	lista.InsertarUltimo("Francia")
	lista.InsertarUltimo("Ecuador")
	lista.InsertarUltimo("Argentina")
	lista.InsertarUltimo("Canada")

	var palabraCorrecta string
	palabraCorrectaPtr := &palabraCorrecta

	lista.Iterar(func(i string) bool {
		*palabraCorrectaPtr = i
		return *palabraCorrectaPtr != "Argentina"
	})

	require.EqualValues(t, "Argentina", palabraCorrecta)

}

// --Test iterador externo

func TestIteradorBorrarPrimero(t *testing.T) {
	lista := TDALista.CrearListaEnlazada[int]()

	iter := lista.Iterador()
	require.PanicsWithValue(t, "El iterador termino de iterar", func() { iter.Borrar() })

	lista.InsertarUltimo(1)
	lista.InsertarUltimo(2)
	lista.InsertarUltimo(3)

	iter = lista.Iterador()

	require.EqualValues(t, 1, iter.Borrar())
	require.EqualValues(t, 2, iter.VerActual())

	require.EqualValues(t, 2, iter.Borrar())
	require.EqualValues(t, 3, iter.VerActual())

	require.EqualValues(t, 3, iter.Borrar())
	require.PanicsWithValue(t, "El iterador termino de iterar", func() { iter.VerActual() })

}

func TestIteradorBorrarMedio(t *testing.T) {
	lista := TDALista.CrearListaEnlazada[int]()

	lista.InsertarUltimo(1)
	lista.InsertarUltimo(343)
	lista.InsertarUltimo(2)
	lista.InsertarUltimo(3)

	iter := lista.Iterador()

	iter.Siguiente() //343
	require.EqualValues(t, 343, iter.Borrar())

	require.EqualValues(t, 2, iter.VerActual())
	require.EqualValues(t, 3, lista.Largo())

	//lista= 1->2->3->nil

	i := 1
	for iter := lista.Iterador(); iter.HaySiguiente(); iter.Siguiente() {
		require.EqualValues(t, i, iter.VerActual())
		i++
	}

}

func TestIteradorBorrarUltimo(t *testing.T) {
	lista := TDALista.CrearListaEnlazada[int]()

	lista.InsertarUltimo(1)
	lista.InsertarUltimo(2)
	lista.InsertarUltimo(3)

	for iter := lista.Iterador(); iter.HaySiguiente(); iter.Siguiente() {
		if iter.VerActual() == lista.VerUltimo() {
			require.EqualValues(t, 3, iter.VerActual())
			require.EqualValues(t, 3, iter.Borrar())
			break
		}
	}

	iter := lista.Iterador()

	require.EqualValues(t, 1, iter.VerActual())
	iter.Siguiente()
	require.EqualValues(t, 2, iter.VerActual())
	iter.Siguiente()

	require.PanicsWithValue(t, "El iterador termino de iterar", func() { iter.VerActual() })

}

func TestIteradorInsertarPrimero(t *testing.T) {
	lista := TDALista.CrearListaEnlazada[int]()

	iter := lista.Iterador()
	iter.Insertar(0)
	require.EqualValues(t, 1, lista.Largo())
	require.EqualValues(t, 0, iter.VerActual())
	require.EqualValues(t, 0, lista.VerPrimero())
	require.EqualValues(t, 0, lista.VerUltimo())

	lista.InsertarUltimo(1)
	lista.InsertarUltimo(2)
	lista.InsertarUltimo(3)
	require.EqualValues(t, 0, lista.VerPrimero())
	require.EqualValues(t, 3, lista.VerUltimo())

	iter = lista.Iterador()

	require.EqualValues(t, 4, lista.Largo())
	require.EqualValues(t, 0, iter.VerActual())

	iter.Insertar(-1) //-1 -> 0 -> 1 -> 2 -> 3
	require.EqualValues(t, 5, lista.Largo())
	require.EqualValues(t, -1, iter.VerActual())
	require.EqualValues(t, -1, lista.VerPrimero())

	iter.Siguiente() //0
	require.EqualValues(t, 0, iter.VerActual())
	iter.Siguiente() //1
	require.EqualValues(t, 1, iter.VerActual())
	iter.Siguiente() //2
	require.EqualValues(t, 2, iter.VerActual())
	iter.Siguiente() //3
	require.EqualValues(t, 3, iter.VerActual())
	iter.Siguiente() //nil

	require.PanicsWithValue(t, "El iterador termino de iterar", func() { iter.Siguiente() })

}

func TestIteradorInsertarMedio(t *testing.T) {
	lista := TDALista.CrearListaEnlazada[int]()

	lista.InsertarUltimo(1)
	lista.InsertarUltimo(3)
	lista.InsertarUltimo(4)

	iter := lista.Iterador()

	iter.Siguiente() //3
	iter.Insertar(2)
	require.EqualValues(t, 2, iter.VerActual())
	require.EqualValues(t, 4, lista.Largo())

	//lista= 1->2->3->4->nil

	i := 1
	for iter := lista.Iterador(); iter.HaySiguiente(); iter.Siguiente() {
		require.EqualValues(t, i, iter.VerActual())
		i++
	}

}

func TestIteradorInsertarUltimo(t *testing.T) {
	lista := TDALista.CrearListaEnlazada[int]()

	lista.InsertarUltimo(0)
	lista.InsertarUltimo(1)
	lista.InsertarUltimo(2)

	i := 0
	for iter := lista.Iterador(); iter.HaySiguiente(); iter.Siguiente() {
		require.EqualValues(t, i, iter.VerActual())
		if iter.VerActual() == lista.VerUltimo() {
			iter.Insertar(3)
			break
		}
		i++
	}

	require.EqualValues(t, 4, lista.Largo())
	require.EqualValues(t, 2, lista.VerUltimo())

	iter := lista.Iterador()

	require.EqualValues(t, 0, iter.VerActual())
	iter.Siguiente()
	require.EqualValues(t, 1, iter.VerActual())
	iter.Siguiente()
	require.EqualValues(t, 3, iter.VerActual())
	iter.Siguiente()
	require.EqualValues(t, 2, iter.VerActual())
	iter.Siguiente()

	require.PanicsWithValue(t, "El iterador termino de iterar", func() { iter.Siguiente() })

}
