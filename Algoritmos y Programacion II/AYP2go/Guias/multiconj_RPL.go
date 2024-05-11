package multiconj

type multiConj[K comparable] struct {
    hashInterno Diccionario[K, int]
}

func CrearMulticonjunto[K comparable]() MultiConjunto[K] {
    nuevo := new(multiConj[K])
    nuevo.hashInterno = CrearHash[K, int]()
    return nuevo
}

func (conj multiConj[K]) Guardar(elem K) {
    if conj.hashInterno.Pertenece(elem) {
        conj.hashInterno.Guardar(elem, conj.hashInterno.Obtener(elem) + 1)
    } else {
        conj.hashInterno.Guardar(elem, 1)
    }
}

func (conj multiConj[K]) Pertenece(elem K) bool {
    if ! conj.hashInterno.Pertenece(elem) || conj.hashInterno.Obtener(elem) == 0 {
        return false
    }
    return true
}

func (conj multiConj[K]) Borrar(elem K) {
    if conj.hashInterno.Pertenece(elem) && conj.hashInterno.Obtener(elem) > 0 {
        conj.hashInterno.Guardar(elem, conj.hashInterno.Obtener - 1)
    }
}