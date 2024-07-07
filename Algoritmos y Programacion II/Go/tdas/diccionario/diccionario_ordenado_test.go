package diccionario_test

import (
	"fmt"
	"github.com/stretchr/testify/require"
	TDADiccionarioOrdenado "tdas/diccionario"
	"testing"
)

var TAMS_VOLUMEN_ARBOL = []int{12500, 25000}

func comparacionString(str1 string, str2 string) int {
	if len(str1) == len(str2) {
		return 0
	}
	if len(str1) > len(str2) {
		return 1
	}
	return -1
}

func comparacionStringParaVolumen(str1 string, str2 string) int {
	if str1 == str2 {
		return 0
	} else if len(str1) > len(str2) {
		return 1
	}
	return -1
}

func comparacionInt(int1 int, int2 int) int {
	if int1 == int2 {
		return 0
	}
	if int1 > int2 {
		return 1
	}
	return -1
}

func TestDiccionarioOrdenadoVacio(t *testing.T) {
	t.Log("Comprueba que Arbol vacio no tiene claves")
	abb := TDADiccionarioOrdenado.CrearABB[string, string](comparacionString)
	require.EqualValues(t, 0, abb.Cantidad())
	require.False(t, abb.Pertenece("A"))
	require.PanicsWithValue(t, "La clave no pertenece al diccionario", func() { abb.Obtener("A") })
	require.PanicsWithValue(t, "La clave no pertenece al diccionario", func() { abb.Borrar("A") })
}

func TestArbolUnElement(t *testing.T) {
	t.Log("Comprueba que Arbol con un elemento tiene esa Clave, unicamente")
	abb := TDADiccionarioOrdenado.CrearABB[string, int](comparacionString)
	abb.Guardar("A", 10)
	require.EqualValues(t, 1, abb.Cantidad())
	require.True(t, abb.Pertenece("A"))
	require.False(t, abb.Pertenece("AA"))
	require.EqualValues(t, 10, abb.Obtener("A"))
	require.PanicsWithValue(t, "La clave no pertenece al diccionario", func() { abb.Obtener("BB") })
}

func TestDiccionarioOrdenadoGuardarMismaClave(t *testing.T) {
	t.Log("Guarda algunos pocos elementos en el arbol, y se comprueba que se actualiza el valor de una misma clave")
	clave1 := "Gato"
	clave2 := "Perro"
	valor1 := "miau"
	valor2 := "guau"
	claves := []string{clave1, clave2}
	valores := []string{valor1, valor2}

	abb := TDADiccionarioOrdenado.CrearABB[string, string](comparacionString)
	require.False(t, abb.Pertenece(claves[0]))
	abb.Guardar(claves[0], valores[0])
	require.EqualValues(t, 1, abb.Cantidad())
	require.True(t, abb.Pertenece(claves[0]))
	require.EqualValues(t, valores[0], abb.Obtener(claves[0]))

	abb.Guardar(claves[0], valores[1])
	require.EqualValues(t, 1, abb.Cantidad())
	require.True(t, abb.Pertenece(claves[0]))
	require.EqualValues(t, valores[1], abb.Obtener(claves[0]))
}

func TestDiccionarioOrdenadoGuardar(t *testing.T) {
	t.Log("Guarda algunos pocos elementos en el arbol, y se comprueba que en todo momento funciona acorde")

	clave1 := 5
	clave2 := 2
	clave3 := 1
	clave4 := 7
	clave5 := 6
	clave6 := 8
	valor1 := "cinco"
	valor2 := "dos"
	valor3 := "uno"
	valor4 := "siete"
	valor5 := "seis"
	valor6 := "ocho"
	claves := []int{clave1, clave2, clave3, clave4, clave5, clave6}
	valores := []string{valor1, valor2, valor3, valor4, valor5, valor6}

	abbNum := TDADiccionarioOrdenado.CrearABB[int, string](comparacionInt)

	require.False(t, abbNum.Pertenece(claves[0]))
	abbNum.Guardar(claves[0], valores[0])
	require.EqualValues(t, 1, abbNum.Cantidad())
	require.True(t, abbNum.Pertenece(claves[0]))
	require.EqualValues(t, valores[0], abbNum.Obtener(claves[0]))

	require.False(t, abbNum.Pertenece(claves[1]))
	abbNum.Guardar(claves[1], valores[1])
	require.EqualValues(t, 2, abbNum.Cantidad())
	require.True(t, abbNum.Pertenece(claves[1]))
	require.EqualValues(t, valores[1], abbNum.Obtener(claves[1]))

	require.False(t, abbNum.Pertenece(claves[2]))
	abbNum.Guardar(claves[2], valores[2])
	require.EqualValues(t, 3, abbNum.Cantidad())
	require.True(t, abbNum.Pertenece(claves[2]))
	require.EqualValues(t, valores[2], abbNum.Obtener(claves[2]))

	require.False(t, abbNum.Pertenece(claves[3]))
	abbNum.Guardar(claves[3], valores[3])
	require.EqualValues(t, 4, abbNum.Cantidad())
	require.True(t, abbNum.Pertenece(claves[3]))
	require.EqualValues(t, valores[3], abbNum.Obtener(claves[3]))

	require.False(t, abbNum.Pertenece(claves[4]))
	abbNum.Guardar(claves[4], valores[4])
	require.EqualValues(t, 5, abbNum.Cantidad())
	require.True(t, abbNum.Pertenece(claves[4]))
	require.EqualValues(t, valores[4], abbNum.Obtener(claves[4]))

	require.False(t, abbNum.Pertenece(claves[5]))
	abbNum.Guardar(claves[5], valores[5])
	require.EqualValues(t, 6, abbNum.Cantidad())
	require.True(t, abbNum.Pertenece(claves[5]))
	require.EqualValues(t, valores[5], abbNum.Obtener(claves[5]))
}

func TestDiccionarioOrdenadoBorrar(t *testing.T) {
	t.Log("Guarda algunos pocos elementos en el diccionario ordenado, y se los borra, revisando que en todo momento " +
		"el diccionario se comporte de manera adecuada")
	clave1 := "Gatos"
	clave2 := "Perros"
	clave3 := "Vaca"
	valor1 := "miau"
	valor2 := "guau"
	valor3 := "moo"
	claves := []string{clave1, clave2, clave3}
	valores := []string{valor1, valor2, valor3}
	abb := TDADiccionarioOrdenado.CrearABB[string, string](comparacionString)

	require.False(t, abb.Pertenece(claves[0]))
	abb.Guardar(claves[0], valores[0])
	abb.Guardar(claves[1], valores[1])
	abb.Guardar(claves[2], valores[2])

	require.True(t, abb.Pertenece(claves[2]))
	require.EqualValues(t, valores[2], abb.Borrar(claves[2]))
	require.PanicsWithValue(t, "La clave no pertenece al diccionario", func() { abb.Borrar(claves[2]) })
	require.EqualValues(t, 2, abb.Cantidad())
	require.False(t, abb.Pertenece(claves[2]))

	require.True(t, abb.Pertenece(claves[0]))
	require.EqualValues(t, valores[0], abb.Borrar(claves[0]))
	require.PanicsWithValue(t, "La clave no pertenece al diccionario", func() { abb.Borrar(claves[0]) })
	require.EqualValues(t, 1, abb.Cantidad())
	require.False(t, abb.Pertenece(claves[0]))
	require.PanicsWithValue(t, "La clave no pertenece al diccionario", func() { abb.Obtener(claves[0]) })

	require.True(t, abb.Pertenece(claves[1]))
	require.EqualValues(t, valores[1], abb.Borrar(claves[1]))
	require.PanicsWithValue(t, "La clave no pertenece al diccionario", func() { abb.Borrar(claves[1]) })
	require.EqualValues(t, 0, abb.Cantidad())
	require.False(t, abb.Pertenece(claves[1]))
	require.PanicsWithValue(t, "La clave no pertenece al diccionario", func() { abb.Obtener(claves[1]) })
}

func TestClaveVaciaArbol(t *testing.T) {
	t.Log("Guardamos una clave vacía (i.e. \"\") y deberia funcionar sin problemas")
	abb := TDADiccionarioOrdenado.CrearABB[string, string](comparacionString)
	clave := ""
	abb.Guardar(clave, clave)
	require.True(t, abb.Pertenece(clave))
	require.EqualValues(t, 1, abb.Cantidad())
	require.EqualValues(t, clave, abb.Obtener(clave))
}

func buscarArbol(clave string, claves []string) int {
	for i, c := range claves {
		if c == clave {
			return i
		}
	}
	return -1
}

func TestIteradorInternoArbolClaves(t *testing.T) {
	t.Log("Valida que todas las claves sean recorridas (y una única vez) con el iterador interno")
	clave1 := "Gato"
	clave2 := "Perros"
	clave3 := "Vacas"
	claves := []string{clave1, clave2, clave3}
	abb := TDADiccionarioOrdenado.CrearABB[string, *int](comparacionString)
	abb.Guardar(claves[0], nil)
	abb.Guardar(claves[1], nil)
	abb.Guardar(claves[2], nil)

	cs := []string{"", "", ""}
	cantidad := 0
	cantPtr := &cantidad

	abb.Iterar(func(clave string, dato *int) bool {
		cs[cantidad] = clave
		*cantPtr = *cantPtr + 1
		return true
	})

	require.EqualValues(t, 3, cantidad)
	require.NotEqualValues(t, -1, buscarArbol(cs[0], claves))
	require.NotEqualValues(t, -1, buscarArbol(cs[1], claves))
	require.NotEqualValues(t, -1, buscarArbol(cs[2], claves))
	require.NotEqualValues(t, cs[0], cs[1])
	require.NotEqualValues(t, cs[0], cs[2])
	require.NotEqualValues(t, cs[2], cs[1])
}

func TestIteradorInternoRangoArbolValores(t *testing.T) {
	t.Log("Valida que sea correcto el comportamiento del iterador interno por rango")
	abb := TDADiccionarioOrdenado.CrearABB[int, string](comparacionInt)
	c1, c2, c3, c4, c5, c6, c7 := 1, 2, 3, 4, 5, 6, 7

	abb.Guardar(c3, "c3")
	abb.Guardar(c6, "c6")
	abb.Guardar(c4, "c4")
	abb.Guardar(c1, "c1")
	abb.Guardar(c5, "c5")
	abb.Guardar(c7, "c7")
	abb.Guardar(c2, "c2")

	// TestIterarABBEnRango: Iterar poniendo un rango de elementos aceptable
	cad1 := ""
	c8 := 8
	abb.IterarRango(&c2, &c8, func(clave int, dato string) bool {
		cad1 += dato
		return true
	})
	cad1Esperada := "c2c3c4c5c6c7"
	require.EqualValues(t, cad1Esperada, cad1)

	// TestIterarRangoSinDesde: Iterar poniendo un rango de elementos pero sin un desde (=nil)
	cad2 := ""
	abb.IterarRango(nil, &c6, func(clave int, dato string) bool {
		cad2 += dato
		return true
	})
	cad2Esperada := "c1c2c3c4c5c6"
	require.EqualValues(t, cad2Esperada, cad2)

	// TestIterarEnRangoIncluyeUnoSolo: Iteramos con rango pero con un rango que termina incluyendo a un único elemento
	cad3 := ""
	abb.IterarRango(&c4, &c4, func(clave int, dato string) bool {
		cad3 += dato
		return true
	})
	cad3Esperada := "c4"
	require.EqualValues(t, cad3Esperada, cad3)
}

func TestIteradorInternoRangoCortaAntes(t *testing.T) {
	t.Log("Valida que el cuando la funcion visitar devuelve false no se sigue aplicando al resto de nodos")
	abb := TDADiccionarioOrdenado.CrearABB[int, string](comparacionInt)
	clave5 := 5
	clave3 := 3
	clave7 := 7
	clave6 := 6
	clave9 := 9
	clave1 := 1
	abb.Guardar(clave5, "cinco")
	abb.Guardar(clave3, "tres")
	abb.Guardar(clave7, "siete")
	abb.Guardar(clave6, "seis")
	abb.Guardar(clave9, "nueve")
	abb.Guardar(clave1, "uno")

	cont := 0
	contPtr := &cont
	abb.IterarRango(&clave3, &clave6, func(clave int, dato string) bool {
		if dato != "siete" {
			*contPtr += clave
			return true
		}
		return false
	})

	require.EqualValues(t, 14, cont)
}

func TestIteradorInternoArbolValoresConBorrados(t *testing.T) {
	t.Log("Valida que los datos sean recorridas correctamente (y una única vez) con el iterador interno, sin encontrar datos borrados")
	clave0 := "Elefantesssss"
	clave1 := "Gato"
	clave2 := "Perros"
	clave3 := "Vacas"
	clave4 := "Burrito"
	clave5 := "Hamsters"

	abb := TDADiccionarioOrdenado.CrearABB[string, int](comparacionString)
	abb.Guardar(clave0, 7)
	abb.Guardar(clave3, 6)
	abb.Guardar(clave4, 2)
	abb.Guardar(clave2, 3)
	abb.Guardar(clave5, 4)
	abb.Guardar(clave1, 5)

	abb.Borrar(clave0)

	factorial := 1
	ptrFactorial := &factorial
	abb.Iterar(func(clave string, dato int) bool {
		*ptrFactorial *= dato
		return true
	})

	require.EqualValues(t, 720, factorial)
}

func TestIteradorExternoRangoVacio(t *testing.T) {
	abb := TDADiccionarioOrdenado.CrearABB[string, int](comparacionString)

	clave1 := "siete"
	clave2 := "uno"

	iter := abb.IteradorRango(&clave1, &clave2)

	require.False(t, iter.HaySiguiente())
}

func TestIteradorRangoExterno(t *testing.T) {
	t.Log("Valida que sea correcto el comportamiento del iterador externo por rango")
	abb := TDADiccionarioOrdenado.CrearABB[int, string](comparacionInt)
	c7, c9, c5, c1, c6, c12, c10 := 7, 9, 5, 1, 6, 12, 10
	abb.Guardar(c7, "siete")
	abb.Guardar(c9, "nueve")
	abb.Guardar(c5, "cinco")
	abb.Guardar(c1, "uno")
	abb.Guardar(c6, "seis")
	abb.Guardar(c12, "doce")
	abb.Guardar(c10, "diez")

	suma := 0 // 5 + 6 + 7 + 9 + 10 = 37

	for iter := abb.IteradorRango(&c5, &c10); iter.HaySiguiente(); iter.Siguiente() {
		clave, _ := iter.VerActual()
		suma += clave
	}
	require.EqualValues(t, 37, suma)

	sumaHastaNueve := 0 // 1 + 5 + 6 + 7 + 9 = 28
	for iter := abb.IteradorRango(nil, &c9); iter.HaySiguiente(); iter.Siguiente() {
		clave, _ := iter.VerActual()
		sumaHastaNueve += clave
	}
	require.EqualValues(t, 28, sumaHastaNueve)

	sumaDesdeNueve := 0 // 9 + 10 + 12 = 31
	for iter := abb.IteradorRango(&c9, nil); iter.HaySiguiente(); iter.Siguiente() {
		clave, _ := iter.VerActual()
		sumaDesdeNueve += clave
	}
	require.EqualValues(t, 31, sumaDesdeNueve)

	sumaTotal := 0 // 1 + 5 + 6 + 7 + 9 + 10 + 12 = 50
	for iter := abb.IteradorRango(nil, nil); iter.HaySiguiente(); iter.Siguiente() {
		clave, _ := iter.VerActual()
		sumaTotal += clave
	}
	require.EqualValues(t, 50, sumaTotal)

	var arrAux []string
	for iter := abb.IteradorRango(&c12, &c12); iter.HaySiguiente(); iter.Siguiente() {
		_, dato := iter.VerActual()
		arrAux = append(arrAux, dato)
	}
	arrAuxEsperado := []string{"doce"}
	require.EqualValues(t, arrAuxEsperado, arrAux)

	var arrAux2 []string
	for iter := abb.IteradorRango(&c9, nil); iter.HaySiguiente(); iter.Siguiente() {
		_, dato := iter.VerActual()
		arrAux2 = append(arrAux2, dato)
	}
	arrAux2Esperado := []string{"nueve", "diez", "doce"}
	require.EqualValues(t, arrAux2Esperado, arrAux2)
}

func TestIteradorExternoArbol(t *testing.T) {
	t.Log("Valida que sea correcto el comportamiento del iterador externo")
	abb := TDADiccionarioOrdenado.CrearABB[int, string](comparacionInt)
	abb.Guardar(7, "")
	abb.Guardar(9, "")
	abb.Guardar(5, "")
	abb.Guardar(1, "")
	abb.Guardar(6, "")
	abb.Guardar(12, "")
	abb.Guardar(10, "")

	sumaTotal := 0 // 1 + 5 + 6 + 7 + 9 + 10 + 12 = 50
	for iter := abb.Iterador(); iter.HaySiguiente(); iter.Siguiente() {
		clave, _ := iter.VerActual()
		sumaTotal += clave
	}
	require.EqualValues(t, 50, sumaTotal)

	sumaPares := 0 // 6 + 12 + 10 = 28
	for iter := abb.Iterador(); iter.HaySiguiente(); iter.Siguiente() {
		clave, _ := iter.VerActual()
		if clave%2 == 0 {
			sumaPares += clave
		}
	}
	require.EqualValues(t, 28, sumaPares)
}

func ejecutarPruebaVolumenArbol(b *testing.B, n int) {
	abb := TDADiccionarioOrdenado.CrearABB[string, int](comparacionStringParaVolumen)

	claves := make([]string, n)
	valores := make([]int, n)

	/* Inserta 'n' parejas en el abb */
	j := 0
	for j < len(claves)-1 {
		claves[j] = fmt.Sprintf("%08d", j+3)
		claves[j+1] = fmt.Sprintf("%08d", j-2)
		valores[j] = j
		valores[j+1] = j + 1
		abb.Guardar(claves[j], valores[j])
		abb.Guardar(claves[j+1], valores[j+1])
		j = j + 2
	}

	/* Verifica que devuelva los valores correctos */
	ok := true
	for i := 0; i < n; i++ {
		ok = abb.Pertenece(claves[i])
		if !ok {
			break
		}
		ok = abb.Obtener(claves[i]) == valores[i]
		if !ok {
			break
		}
	}

	require.True(b, ok, "Pertenece y Obtener con muchos elementos no funciona correctamente")

	/* Verifica que borre y devuelva los valores correctos */
	for i := 0; i < n; i++ {
		ok = abb.Borrar(claves[i]) == valores[i]
		if !ok {
			break
		}
	}

	require.True(b, ok, "Borrar muchos elementos no funciona correctamente")
	require.EqualValues(b, 0, abb.Cantidad())
}

func BenchmarkArbol(b *testing.B) {
	b.Log("Prueba de stress del Diccionario Ordenado. Prueba guardando distinta cantidad de elementos (muy grandes), " +
		"ejecutando muchas veces las pruebas para generar un benchmark. Validamos que podemos obtener y ver " +
		"si pertenece cada una de las claves geeneradas y que luego podemos borrar sin problemas")
	for _, n := range TAMS_VOLUMEN_ARBOL {
		b.Run(fmt.Sprintf("Prueba %d elementos", n), func(b *testing.B) {
			for i := 0; i < b.N; i++ {
				ejecutarPruebaVolumenArbol(b, n)
			}
		})
	}

}

func TestIteradorInternoRangoArbolClaves(t *testing.T) {
	t.Log("Valida que todas las claves sean recorridas (y una única vez) con el iterador interno dado un rango")
	clave1 := "Rinoceronte"
	clave2 := "Perro"
	clave3 := "Vaca"
	clave4 := "Cabras"
	clave5 := "Gallina"
	claves := []string{clave1, clave2, clave3, clave4, clave5}
	abb := TDADiccionarioOrdenado.CrearABB[string, *int](comparacionString)
	abb.Guardar(claves[0], nil)
	abb.Guardar(claves[1], nil)
	abb.Guardar(claves[2], nil)
	abb.Guardar(claves[3], nil)
	abb.Guardar(claves[4], nil)

	clavesIteradas := []string{"", "", "", "", ""}
	cantidad := 0
	cantPtr := &cantidad

	abb.IterarRango(&clave3, &clave1, func(clave string, dato *int) bool {
		clavesIteradas[cantidad] = clave
		*cantPtr = *cantPtr + 1
		return true
	})

	require.EqualValues(t, 5, cantidad)

	cantidad2 := 0
	cantPtr2 := &cantidad2
	abb.IterarRango(nil, &clave5, func(clave string, dato *int) bool {
		clavesIteradas[cantidad2] = clave
		*cantPtr2 = *cantPtr2 + 1
		return true
	})

	require.EqualValues(t, 4, cantidad2)

	cantidad3 := 0
	cantPtr3 := &cantidad3
	abb.IterarRango(&clave2, nil, func(clave string, dato *int) bool {
		clavesIteradas[cantidad3] = clave
		*cantPtr3 = *cantPtr3 + 1
		return true
	})

	require.EqualValues(t, 4, cantidad3)

	cantidad4 := 0
	cantPtr4 := &cantidad4
	abb.IterarRango(nil, nil, func(clave string, dato *int) bool {
		clavesIteradas[cantidad4] = clave
		*cantPtr4 = *cantPtr4 + 1
		return true
	})

	require.EqualValues(t, 5, cantidad4)
}

func TestIterarDiccionarioOrdenadoVacio(t *testing.T) {
	t.Log("Iterar sobre diccionario ordenado vacio es simplemente tenerlo al final")
	abb := TDADiccionarioOrdenado.CrearABB[string, int](comparacionString)
	iter := abb.Iterador()
	require.False(t, iter.HaySiguiente())
	require.PanicsWithValue(t, "El iterador termino de iterar", func() { iter.VerActual() })
	require.PanicsWithValue(t, "El iterador termino de iterar", func() { iter.Siguiente() })
}

func TestDiccionarioIterarArbol(t *testing.T) {
	t.Log("Guardamos 3 valores en un Diccionario Ordenado, e iteramos validando que las claves sean todas diferentes " +
		"pero pertenecientes al diccionario. Además los valores de VerActual y Siguiente van siendo correctos entre sí")
	clave1 := "Rinoceronte"
	clave2 := "Perro"
	clave3 := "Vaca"
	clave4 := "Gato"
	clave5 := "Cabras"
	clave6 := "Gallina"
	valor1 := "nose"
	valor2 := "guau"
	valor3 := "moo"
	valor4 := "miau"
	valor5 := "mee"
	valor6 := "cocoroco"
	claves := []string{clave1, clave2, clave3, clave4, clave5, clave6}
	valores := []string{valor1, valor2, valor3, valor4, valor5, valor6}
	abb := TDADiccionarioOrdenado.CrearABB[string, string](comparacionString)
	abb.Guardar(claves[0], valores[0])
	abb.Guardar(claves[1], valores[1])
	abb.Guardar(claves[2], valores[2])
	abb.Guardar(claves[3], valores[3])
	abb.Guardar(claves[4], valores[4])
	abb.Guardar(claves[5], valores[5])
	iter := abb.Iterador()
	require.True(t, iter.HaySiguiente())

	clavesEnOrden := []string{claves[2], claves[1], claves[4], claves[5], claves[0]}
	for i := 0; iter.HaySiguiente(); i++ {
		clave, _ := iter.VerActual()
		require.EqualValues(t, clavesEnOrden[i], clave)
		iter.Siguiente()
	}
}

func TestIteradorNoLlegaAlFinalArbol(t *testing.T) {
	t.Log("Crea un iterador y no lo avanza. Luego crea otro iterador y lo avanza.")
	clave1 := "Rinoceronte"
	clave2 := "Vaca"
	clave3 := "Perro"
	claves := []string{clave1, clave2, clave3}
	abb := TDADiccionarioOrdenado.CrearABB[string, string](comparacionString)
	abb.Guardar(claves[0], "")
	abb.Guardar(claves[1], "")
	abb.Guardar(claves[2], "")

	abb.Iterador()
	iter2 := abb.Iterador()
	iter2.Siguiente()
	iter3 := abb.Iterador()
	primero, _ := iter3.VerActual()
	iter3.Siguiente()
	segundo, _ := iter3.VerActual()
	iter3.Siguiente()
	tercero, _ := iter3.VerActual()
	iter3.Siguiente()
	require.False(t, iter3.HaySiguiente())
	require.NotEqualValues(t, primero, segundo)
	require.NotEqualValues(t, tercero, segundo)
	require.NotEqualValues(t, primero, tercero)
	require.NotEqualValues(t, -1, buscarArbol(primero, claves))
	require.NotEqualValues(t, -1, buscarArbol(segundo, claves))
	require.NotEqualValues(t, -1, buscarArbol(tercero, claves))
}

func TestPruebaIterarTrasBorradosArbol(t *testing.T) {
	t.Log("Prueba de caja blanca: Esta prueba intenta verificar el comportamiento del abb cuando " +
		"se borran nodos. El abb debe quedar como si nunca se hubiera ingresado el elemento borrado")

	clave1 := "Gato"
	clave2 := "Perros"
	clave3 := "Vacas"

	abb := TDADiccionarioOrdenado.CrearABB[string, string](comparacionString)
	abb.Guardar(clave1, "")
	abb.Guardar(clave2, "")
	abb.Guardar(clave3, "")
	abb.Borrar(clave1)
	abb.Borrar(clave2)
	abb.Borrar(clave3)
	iter := abb.Iterador()

	require.False(t, iter.HaySiguiente())
	require.PanicsWithValue(t, "El iterador termino de iterar", func() { iter.VerActual() })
	require.PanicsWithValue(t, "El iterador termino de iterar", func() { iter.Siguiente() })
	abb.Guardar(clave1, "A")
	iter = abb.Iterador()

	require.True(t, iter.HaySiguiente())
	c1, v1 := iter.VerActual()
	require.EqualValues(t, clave1, c1)
	require.EqualValues(t, "A", v1)
	iter.Siguiente()
	require.False(t, iter.HaySiguiente())
}

func ejecutarPruebasVolumenIteradorArbol(b *testing.B, n int) {
	abb := TDADiccionarioOrdenado.CrearABB[int, int](comparacionInt)

	/* Inserta 'n' parejas en el abb */
	for i := 0; i < n/2; i++ {
		abb.Guardar(i, i)
		abb.Guardar(-i, -i)
	}

	// Prueba de iteración sobre las claves almacenadas.
	iter := abb.Iterador()
	require.True(b, iter.HaySiguiente())

	k := 0

	for k = -(n / 2) + 1; k < n/2; k++ {
		require.True(b, iter.HaySiguiente())
		c1, v1 := iter.VerActual()
		require.EqualValues(b, k, c1)
		require.EqualValues(b, k, v1)
		iter.Siguiente()
	}
	require.EqualValues(b, k, n/2, "No se recorrió todo el largo")
	require.False(b, iter.HaySiguiente(), "El iterador debe estar al final luego de recorrer")
}

func BenchmarkIteradorArbol(b *testing.B) {
	b.Log("Prueba de stress del Iterador del Diccionario. Prueba guardando distinta cantidad de elementos " +
		"(muy grandes) b.N elementos, iterarlos todos sin problemas. Se ejecuta cada prueba b.N veces para generar " +
		"un benchmark")
	for _, n := range TAMS_VOLUMEN_ARBOL {
		b.Run(fmt.Sprintf("Prueba %d elementos", n), func(b *testing.B) {
			for i := 0; i < b.N; i++ {
				ejecutarPruebasVolumenIteradorArbol(b, n)
			}
		})
	}
}
