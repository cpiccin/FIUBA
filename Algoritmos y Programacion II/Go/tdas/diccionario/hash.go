package diccionario

import (
	"fmt"
)

const (
	INITIALCAPACITY      = 7
	VACIO                = 0
	OCUPADO              = 1
	BORRADO              = 2
	HACIARRIBA           = "a"
	HACIABAJO            = "b"
	FACTORDECARGAHASH    = 0.7
	FACTORDEDESCARGAHASH = 0.3
)

type hash[K comparable, V any] struct {
	tabla    []celdaHash[K, V]
	cantidad int
	borrados int
}

type celdaHash[K comparable, V any] struct {
	clave  K
	valor  V
	estado [3]bool
}

func convertirABytes[K comparable](clave K) []byte {
	return []byte(fmt.Sprintf("%v", clave))
}

func mix(a, b, c int) int {
	a -= b
	a -= c
	a ^= (c >> 13)
	b -= c
	b -= a
	b ^= (a << 8)
	c -= a
	c -= b
	c ^= (b >> 13)
	a -= b
	a -= c
	a ^= (c >> 12)
	b -= c
	b -= a
	b ^= (a << 16)
	c -= a
	c -= b
	c ^= (b >> 5)
	a -= b
	a -= c
	a ^= (c >> 3)
	b -= c
	b -= a
	b ^= (a << 10)
	c -= a
	c -= b
	c ^= (b >> 15)
	return c
}

// hashing []byte to int
func hashJenkins(data []byte) int {
	var a, b, c int
	length := len(data)
	for i := 0; i < length; i++ {
		a += int(data[i])
		b += a
		c += b
	}
	return abs(mix(a, b, c))
}

func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}

func crearTablaHash[K comparable, V any](capacidad int) []celdaHash[K, V] {
	tabla := make([]celdaHash[K, V], capacidad)
	for i := 0; i < capacidad; i++ {
		tabla[i].estado[VACIO] = true
	}
	return tabla
}

func CrearHash[K comparable, V any]() Diccionario[K, V] {
	return &hash[K, V]{tabla: crearTablaHash[K, V](INITIALCAPACITY)}
}

// Busca en la tabla pasada por parametro la primera posicion que esté "VACIA",
// buscando desde el index inicial pasado por parametro
func (self *hash[K, V]) seguirBuscandoCeldaVacia(tabla []celdaHash[K, V], index int) int {
	for !tabla[index].estado[VACIO] {
		index++
		if index == len(tabla) {
			index = 0
		}
	}
	return index
}

func (h *hash[K, V]) redimensionar(capacidad int) {
	var index int
	nuevaTablaHash := crearTablaHash[K, V](capacidad)
	for i := 0; i < len(h.tabla); i++ {
		if !h.tabla[i].estado[VACIO] && h.tabla[i].estado[OCUPADO] {
			index = hashJenkins(convertirABytes(h.tabla[i].clave)) % capacidad
			index = h.seguirBuscandoCeldaVacia(nuevaTablaHash, index)
			nuevaTablaHash[index] = h.tabla[i]
		}
	}
	h.borrados = 0
	h.tabla = nuevaTablaHash
}

func (self *hash[K, V]) condicionParaRedimensionar(sentido string) float64 {
	if sentido == HACIARRIBA {
		return float64((self.cantidad + self.borrados) / len(self.tabla))
	}
	return float64(((self.cantidad + self.borrados) * INITIALCAPACITY) / len(self.tabla))
}

// Busca, en la tabla, la clave que sea igual a la pasada por parametro.
// Se usa en los metodos Pertenece()*usando valor bool de retorno* y Obtener()*usando el index int de retorno*
func (self *hash[K, V]) buscarPsoibleIndiceDeClave(clave K) (bool, int) {
	indexPosible := hashJenkins(convertirABytes(clave)) % len(self.tabla)
	for !self.tabla[indexPosible].estado[VACIO] { //hasta encontrar un nil
		//si encuentra uno borrado ignora
		if !self.tabla[indexPosible].estado[BORRADO] {
			if self.tabla[indexPosible].clave == clave {
				return true, indexPosible
			}
		}
		indexPosible++
		if indexPosible == len(self.tabla) { //si llego a la ultima pos vuelve a cero
			indexPosible = 0
		}
	}
	return false, indexPosible
}

func (self *hash[K, V]) Pertenece(clave K) bool {
	res, _ := self.buscarPsoibleIndiceDeClave(clave)
	return res
}

func (self *hash[K, V]) Obtener(clave K) V {
	res, index := self.buscarPsoibleIndiceDeClave(clave)
	if !res {
		panic("La clave no pertenece al diccionario")
	}
	return self.tabla[index].valor
}

func (self *hash[K, V]) Cantidad() int {
	return self.cantidad
}

func (self *hash[K, V]) Guardar(clave K, dato V) {
	if self.condicionParaRedimensionar(HACIARRIBA) >= FACTORDECARGAHASH {
		self.redimensionar(len(self.tabla) * INITIALCAPACITY)
	}

	res, index := self.buscarPsoibleIndiceDeClave(clave)
	if !res {
		self.cantidad++
		self.tabla[index] = celdaHash[K, V]{clave: clave, valor: dato}
		self.tabla[index].estado[OCUPADO] = true
		self.tabla[index].estado[VACIO] = false
		return
	}
	self.tabla[index].valor = dato

}

func (self *hash[K, V]) Borrar(clave K) V {
	res, index := self.buscarPsoibleIndiceDeClave(clave)
	if !res {
		panic("La clave no pertenece al diccionario")
	}
	elemBorrado := self.tabla[index].valor
	self.tabla[index].estado[BORRADO] = true
	self.tabla[index].estado[OCUPADO] = false
	self.cantidad--
	self.borrados++

	if self.condicionParaRedimensionar(HACIABAJO) <= FACTORDEDESCARGAHASH {
		self.redimensionar(len(self.tabla) / INITIALCAPACITY)
	}

	return elemBorrado
}

func (self *hash[K, V]) Iterar(visitar func(clave K, dato V) bool) {
	for i := 0; i < len(self.tabla); i++ {
		if !self.tabla[i].estado[VACIO] && self.tabla[i].estado[OCUPADO] {
			dic := self.tabla[i]
			if !visitar(dic.clave, dic.valor) {
				break
			}
		}
	}
}

type iterDic[K comparable, V any] struct {
	hash   *hash[K, V]
	indice int
	actual *celdaHash[K, V]
}

func (self *hash[K, V]) Iterador() IterDiccionario[K, V] {
	newIter := &iterDic[K, V]{hash: self}
	newIter.seguirBuscandoIndiceValido()
	newIter.actualizarActual()
	return newIter
}

func (iter *iterDic[K, V]) HaySiguiente() bool {
	return iter.actual != nil
}

func (iter *iterDic[K, V]) VerActual() (K, V) {
	iter.verificarIteracion()
	return iter.actual.clave, iter.actual.valor
}

func (iter *iterDic[K, V]) Siguiente() {
	iter.verificarIteracion()
	iter.indice++
	iter.seguirBuscandoIndiceValido()
	iter.actualizarActual()
}

func (iter *iterDic[K, V]) seguirBuscandoIndiceValido() {
	for iter.indice < len(iter.hash.tabla) {
		if iter.hash.tabla[iter.indice].estado[OCUPADO] {
			break
		}
		iter.indice++
	}
}

func (iter *iterDic[K, V]) actualizarActual() {
	if iter.indice == len(iter.hash.tabla) {
		iter.actual = nil
		return
	}
	iter.actual = &iter.hash.tabla[iter.indice]
}

func (iter *iterDic[K, V]) verificarIteracion() {
	if !iter.HaySiguiente() {
		panic("El iterador termino de iterar")
	}
}
