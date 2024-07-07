package admmemoria

import (
	"administracionmemoria/administrador"
)

type Vector struct {
	datos *[]int
}

// CrearVector crea un vector, utilizando el administrador de memoria
func CrearVector(tam int) *Vector {
	vec := administrador.PedirMemoria[Vector]()
	(*vec).datos = administrador.PedirArreglo[int](tam)
	return vec
}

// Redimensionar cambia el tamaño del vector
func (vector *Vector) Redimensionar(tam_nuevo int) {
	vector.datos = administrador.RedimensionarMemoria(vector.datos, tam_nuevo)
}

// Destruir Destruye la memoria asociada al vector
func (vector *Vector) Destruir() {
	administrador.LiberarArreglo(vector.datos)
	administrador.LiberarMemoria(vector)
}

// Largo devuelve el largo de este vector
func (vector Vector) Largo() int {
	return len(*vector.datos)
}

// Guardar guarda el elemento pasado por parámetro en la posición indicada, si esta es válida.
// Si no es válida, entonces entra en pánico con un mensaje "Fuera de rango".
func (vector *Vector) Guardar(pos int, elem int) {
	vector.validaPosicion(pos)
	(*vector.datos)[pos] = elem

}

// Obtener obtiene el elemento guardado en la posición indicada, si esta es válida.
// Si no es válida, entonces entra en pánico con un mensaje "Fuera de rango".
func (vector Vector) Obtener(pos int) int {
	vector.validaPosicion(pos)
	return (*vector.datos)[pos]
}

// Recibe una posicion dentro de un array y la valida.
// Si no corresponde a una posicion válida entra en pánico con un mensaje "Fuera de rango".
func (vector *Vector) validaPosicion(pos int) {
	if pos > vector.Largo()-1 || pos < 0 {
		panic("Fuera de rango")
	}
}
