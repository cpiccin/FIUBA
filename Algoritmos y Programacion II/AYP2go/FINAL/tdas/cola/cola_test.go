package cola_test

import (
	"github.com/stretchr/testify/require"
	TDACola "tdas/cola"
	"testing"
)

func TestColaVacia(t *testing.T) {
	cola := TDACola.CrearColaEnlazada[int]()

	require.True(t, cola.EstaVacia())
	require.PanicsWithValue(t, "La cola esta vacia", func() { cola.VerPrimero() })
	require.PanicsWithValue(t, "La cola esta vacia", func() { cola.Desencolar() })

	cola.Encolar(1)
	require.False(t, cola.EstaVacia())

	require.EqualValues(t, 1, cola.Desencolar())
	require.True(t, cola.EstaVacia())
}

func TestComportamientoFIFO(t *testing.T) {
	cola := TDACola.CrearColaEnlazada[int]()
	cola.Encolar(4)
	cola.Encolar(2)
	cola.Encolar(8)

	require.EqualValues(t, 4, cola.Desencolar())
	require.EqualValues(t, 2, cola.Desencolar())
	require.False(t, cola.EstaVacia())
	require.EqualValues(t, 8, cola.Desencolar())

	cola.Encolar(3)
	cola.Encolar(6)

	require.EqualValues(t, 3, cola.Desencolar())
	require.EqualValues(t, 6, cola.Desencolar())

	require.PanicsWithValue(t, "La cola esta vacia", func() { cola.Desencolar() })
	require.PanicsWithValue(t, "La cola esta vacia", func() { cola.VerPrimero() })
	require.True(t, cola.EstaVacia())
}

func TestVolumen(t *testing.T) {
	cola := TDACola.CrearColaEnlazada[int]()

	for i := 0; i < 10000; i++ {
		cola.Encolar(i + 1) // la cola va del 1 al 10000, 1 es el primero y 10000 el ultimo de la cola
	}

	require.EqualValues(t, 1, cola.VerPrimero())

	for i := 0; i < 7000; i++ {
		cola.Desencolar()
	}

	require.EqualValues(t, 7001, cola.VerPrimero()) // ahora 7001 es el primero y 10000 sigue siendo el ultimo

	for i := 0; i < 2999; i++ {
		cola.Desencolar()
	}

	require.EqualValues(t, 10000, cola.VerPrimero())
	require.False(t, cola.EstaVacia())
	require.EqualValues(t, 10000, cola.Desencolar())
	require.True(t, cola.EstaVacia())
}

func TestEstaVacia(t *testing.T) {
	cola := TDACola.CrearColaEnlazada[string]()

	require.True(t, cola.EstaVacia())
	cola.Encolar("Panama")
	require.False(t, cola.EstaVacia())
	cola.Desencolar()
	require.True(t, cola.EstaVacia())
}

func TestPanics(t *testing.T) {
	cola := TDACola.CrearColaEnlazada[bool]()
	require.PanicsWithValue(t, "La cola esta vacia", func() { cola.VerPrimero() })
	require.PanicsWithValue(t, "La cola esta vacia", func() { cola.Desencolar() })
}

func TestVerPrimeroNoDesencola(t *testing.T) {
	cola := TDACola.CrearColaEnlazada[string]()
	cola.Encolar("Quito")
	cola.VerPrimero()
	require.False(t, cola.EstaVacia())
}

func TestDistintosTiposDeDatos(t *testing.T) {
	cola_auxiliar := TDACola.CrearColaEnlazada[string]()

	cola_int := TDACola.CrearColaEnlazada[int]()
	cola_float64 := TDACola.CrearColaEnlazada[float64]()
	cola_string := TDACola.CrearColaEnlazada[string]()
	cola_bool := TDACola.CrearColaEnlazada[bool]()
	cola_cola := TDACola.CrearColaEnlazada[TDACola.Cola[string]]()

	cola_int.Encolar(2)
	cola_float64.Encolar(4.32)
	cola_string.Encolar("Marambio")
	cola_bool.Encolar(false)
	cola_cola.Encolar(cola_auxiliar)

	require.Equal(t, 2, cola_int.Desencolar(), "El primero debe ser 2")
	require.Equal(t, 4.32, cola_float64.Desencolar(), "El primero debe ser 4.32")
	require.Equal(t, "Marambio", cola_string.Desencolar(), "El primero debe ser 'Marambio'")
	require.Equal(t, false, cola_bool.Desencolar(), "El primero debe ser 'false'")
	require.Equal(t, cola_auxiliar, cola_cola.Desencolar(), "El primero debe ser la cola_auxiliar")

	require.True(t, cola_int.EstaVacia())
	require.True(t, cola_float64.EstaVacia())
	require.True(t, cola_string.EstaVacia())
	require.True(t, cola_bool.EstaVacia())
	require.True(t, cola_cola.EstaVacia())
}

func TestComportamientoColaVaciada(t *testing.T) {
	cola := TDACola.CrearColaEnlazada[int]()

	cola.Encolar(1)
	cola.Encolar(4)
	cola.Encolar(8)
	require.False(t, cola.EstaVacia())
	cola.Desencolar()
	cola.Desencolar()
	cola.Desencolar()

	require.True(t, cola.EstaVacia())
	require.PanicsWithValue(t, "La cola esta vacia", func() { cola.VerPrimero() })
	require.PanicsWithValue(t, "La cola esta vacia", func() { cola.Desencolar() })

	cola.Encolar(1)
	require.False(t, cola.EstaVacia())

	require.EqualValues(t, 1, cola.Desencolar())
	require.True(t, cola.EstaVacia())
}

func TestEncolarElementosIguales(t *testing.T) {
	cola := TDACola.CrearColaEnlazada[int]()

	cola.Encolar(4)
	cola.Encolar(4)
	cola.Encolar(4)
	require.EqualValues(t, 4, cola.VerPrimero())

	cola.Desencolar()
	require.False(t, cola.EstaVacia())
	cola.Desencolar()
	cola.Desencolar()
	require.True(t, cola.EstaVacia())

	require.PanicsWithValue(t, "La cola esta vacia", func() { cola.Desencolar() })
	require.PanicsWithValue(t, "La cola esta vacia", func() { cola.VerPrimero() })
}
