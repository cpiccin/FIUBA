package pila_test

import (
	"github.com/stretchr/testify/require"
	TDAPila "tdas/pila"
	"testing"
)

func TestPilaVacia(t *testing.T) {

	pila := TDAPila.CrearPilaDinamica[int]()
	require.True(t, pila.EstaVacia())
	require.PanicsWithValue(t, "La pila esta vacia", func() { pila.VerTope() })
	require.PanicsWithValue(t, "La pila esta vacia", func() { pila.Desapilar() })

	require.NotNil(t, pila)

	pila.Apilar(1)
	require.False(t, pila.EstaVacia()) // deja de estar vacia

	pila.Desapilar()
	require.True(t, pila.EstaVacia()) // vuelve a estar vacia
}

func TestComportamientoDePila(t *testing.T) {

	pila := TDAPila.CrearPilaDinamica[string]()
	pila.Apilar("uno")
	pila.Apilar("dos")
	pila.Apilar("tres")

	require.EqualValues(t, "tres", pila.Desapilar())
	require.EqualValues(t, "dos", pila.Desapilar())
	require.EqualValues(t, "uno", pila.Desapilar())

	pila.Apilar("tres")
	pila.Apilar("dos")

	require.EqualValues(t, "dos", pila.Desapilar())
	require.EqualValues(t, "tres", pila.Desapilar())
	require.PanicsWithValue(t, "La pila esta vacia", func() { pila.Desapilar() })
	require.NotNil(t, pila)
}

func TestVolumen(t *testing.T) {
	pila := TDAPila.CrearPilaDinamica[int]()

	for i := 0; i < 10000; i++ { // pila de elementos ordenados crecientes hasta 10000 pila.cantidad = 10000
		pila.Apilar(i + 1)
	}

	require.EqualValues(t, 10000, pila.VerTope()) // el tope tiene que ser 10000

	for i := 0; i < 9500; i++ { // Desapilo 9500 valores
		pila.Desapilar()
	}

	require.EqualValues(t, 500, pila.VerTope()) // el tope debe ser 500
}

func TestEstaVacia(t *testing.T) {
	pila := TDAPila.CrearPilaDinamica[string]()
	require.True(t, pila.EstaVacia())
	pila.Apilar("Austria")
	require.False(t, pila.EstaVacia())
	pila.Desapilar()
	require.True(t, pila.EstaVacia())
}

func TestPanics(t *testing.T) {
	pila_vacia := TDAPila.CrearPilaDinamica[int]()
	require.PanicsWithValue(t, "La pila esta vacia", func() { pila_vacia.VerTope() })
	require.PanicsWithValue(t, "La pila esta vacia", func() { pila_vacia.Desapilar() })
}

func TestComportamientoDesapilarVerTope(t *testing.T) {

	pila1 := TDAPila.CrearPilaDinamica[int]()
	pila2 := TDAPila.CrearPilaDinamica[int]()

	for i := 1; i <= 5; i++ { //apilo 5 elementos
		pila1.Apilar(i)
		pila2.Apilar(5 - i)
	}

	require.EqualValues(t, 5, pila1.VerTope()) //[1,2,3,4,5]
	require.EqualValues(t, 0, pila2.VerTope()) //[4,3,2,1,0]

	require.EqualValues(t, 5, pila1.Desapilar()) //[1,2,3,4]
	require.EqualValues(t, 0, pila2.Desapilar()) //[4,3,2,1]

	require.EqualValues(t, 4, pila1.VerTope()) //[1,2,3,4]
	require.EqualValues(t, 1, pila2.VerTope()) //[4,3,2,1]

	for i := 1; i < 5; i++ { // pila1.cantidad = 4
		pila1.Desapilar()
	}
	// Se comporta como si fuese una pila recien creada
	require.True(t, pila1.EstaVacia())
	require.PanicsWithValue(t, "La pila esta vacia", func() { pila1.Desapilar() })
	require.PanicsWithValue(t, "La pila esta vacia", func() { pila1.VerTope() })
}

func TestDistintosTiposDeDatos(t *testing.T) {
	pila1 := TDAPila.CrearPilaDinamica[int]()

	pila_int := TDAPila.CrearPilaDinamica[int]()                // pila de ints
	pila_string := TDAPila.CrearPilaDinamica[string]()          // pila de strings
	pila_bool := TDAPila.CrearPilaDinamica[bool]()              // pila de booleanos
	pila_pila := TDAPila.CrearPilaDinamica[TDAPila.Pila[int]]() // pila de Pilas[int]

	pila_int.Apilar(6)
	pila_string.Apilar("Roma")
	pila_bool.Apilar(true)
	pila_pila.Apilar(pila1)

	require.Equal(t, 6, pila_int.VerTope(), "El tope debe ser 6")
	require.Equal(t, "Roma", pila_string.VerTope(), "El tope debe ser 'Roma'")
	require.Equal(t, true, pila_bool.VerTope(), "El tope debe ser 'true'")
	require.Equal(t, pila1, pila_pila.VerTope(), "El tope debe ser la pila1")
}

func TestVerTopeNoModificaPila(t *testing.T) {
	pila := TDAPila.CrearPilaDinamica[int]()
	pila.Apilar(284)
	pila.VerTope() // devuelve el tope como Desapilar() pero no se tiene que vaciar la pila
	require.False(t, pila.EstaVacia())
}
