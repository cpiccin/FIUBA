package diccionario

import (
	pila "tdas/pila"
	cola "tdas/cola"
)

//---STRUCTS---

type abb[K comparable, V any] struct {
	raiz     *nodoAbb[K, V]
	cantidad int
	funcCmp  func(K, K) int
}

type nodoAbb[K comparable, V any] struct {
	izq   *nodoAbb[K, V]
	der   *nodoAbb[K, V]
	clave K
	dato  V
}

//---Primitivas Crear---

func CrearABB[K comparable, V any](funcion_cmp func(K, K) int) DiccionarioOrdenado[K, V] {
	return &abb[K, V]{funcCmp: funcion_cmp}
}

func crearNodoAb[K comparable, V any](clave K, dato V) *nodoAbb[K, V] {
	return &nodoAbb[K, V]{clave: clave, dato: dato}
}

//---Primitivas Auxiliares---

func (ab *abb[K, V]) buscarClaveArbol(clave K) (bool, *nodoAbb[K, V]) {
	if ab.raiz == nil {
		return false, nil
	}
	if ab.funcCmp(ab.raiz.clave, clave) > 0 {
		return ab.raiz.izq.buscarClaveNodo(clave, ab.funcCmp, ab.raiz)
	} else if ab.funcCmp(ab.raiz.clave, clave) == 0 {
		return true, ab.raiz
	}
	return ab.raiz.der.buscarClaveNodo(clave, ab.funcCmp, ab.raiz)
}

func (nodo *nodoAbb[K, V]) buscarClaveNodo(clave K, cmp func(K, K) int, anterior *nodoAbb[K, V]) (bool, *nodoAbb[K, V]) {
	if nodo == nil {
		return false, anterior
	}
	anterior = nodo
	if cmp(nodo.clave, clave) == 0 {
		return true, nodo
	}
	if cmp(nodo.clave, clave) > 0 {
		return nodo.izq.buscarClaveNodo(clave, cmp, anterior)
	} else {
		return nodo.der.buscarClaveNodo(clave, cmp, anterior)
	}
}

func (nodo *nodoAbb[K, V]) ultimo() *nodoAbb[K, V] {
	if nodo.der == nil {
		return nodo
	}
	return nodo.der.ultimo()
}

func (nodo *nodoAbb[K, V]) primero() *nodoAbb[K, V] {
	if nodo.izq == nil {
		return nodo
	}
	return nodo.izq.primero()
}

func (nodo *nodoAbb[K, V]) borrarNodo(clave K, padre *nodoAbb[K, V], cmp func(K, K) int) *nodoAbb[K, V] {
	if nodo == nil {
		return nil
	}

	if cmp(nodo.clave, clave) > 0 {
		nodo.izq = nodo.izq.borrarNodo(clave, nodo, cmp)
	} else if cmp(nodo.clave, clave) < 0 {
		nodo.der = nodo.der.borrarNodo(clave, nodo, cmp)
	} else {
		if nodo.izq == nil && nodo.der == nil { // el que se borra no tiene hijos
			return nil
		} else if nodo.izq == nil { // el que se borra tiene un solo hijo que es der
			return nodo.der
		} else if nodo.der == nil { // el que se borra tiene un solo hijo que es izq
			return nodo.izq
		} else { // el que se borra tiene dos hijos
			if nodo.der.izq != nil {
				sucesor := nodo.obtenerSucesor()
				nodo.clave, nodo.dato = sucesor.clave, sucesor.dato
				nodo.der = nodo.der.borrarNodo(sucesor.clave, nodo, cmp)
			} else { // si el hijo mayor no tiene hijo menor entonces es el nuevo padre
				nodo.clave, nodo.dato = nodo.der.clave, nodo.der.dato
				nodo.der = nodo.der.der
			}
		}
	}
	return nodo
}

func (nodo *nodoAbb[K, V]) obtenerSucesor() *nodoAbb[K, V] {
	actual := nodo.der
	for actual.izq != nil { // busco el mas izquierdo del hijo mayor para que sea el nuevo padre y se mantenga el orden
		actual = actual.izq
	}
	return actual
}

//---Primitivas Principales---

func (arbol *abb[K, V]) Pertenece(clave K) bool {
	res, _ := arbol.buscarClaveArbol(clave)
	return res

}

func (arbol *abb[K, V]) Obtener(clave K) V {
	res, nodo := arbol.buscarClaveArbol(clave)
	if !res {
		panic("La clave no pertenece al diccionario")
	}
	return nodo.dato
}

func (arbol *abb[K, V]) Cantidad() int {
	return arbol.cantidad
}

func (arbol *abb[K, V]) Guardar(clave K, dato V) {
	res, nodo := arbol.buscarClaveArbol(clave)
	if arbol.cantidad == 0 {
		arbol.raiz = &nodoAbb[K, V]{clave: clave, dato: dato}
		arbol.cantidad++
		return
	}
	if !res {
		nuevoNodoAb := crearNodoAb[K, V](clave, dato)
		if arbol.funcCmp(nodo.clave, nuevoNodoAb.clave) > 0 {
			nodo.izq = nuevoNodoAb
		} else {
			nodo.der = nuevoNodoAb
		}
		arbol.cantidad++
		return
	}
	nodo.dato = dato
}

func (arbol *abb[K, V]) Borrar(clave K) V {
	res, nodo := arbol.buscarClaveArbol(clave)
	if !res {
		panic("La clave no pertenece al diccionario")
	}
	nodoBorrado := nodo.dato
	nodoNuevaRaiz := arbol.raiz.borrarNodo(clave, nil, arbol.funcCmp)
	arbol.raiz = nodoNuevaRaiz
	arbol.cantidad--
	return nodoBorrado
}

//---ITERADORES---

//--Iteradores Internos--

func (arbol *abb[K, V]) IterarRango(desde *K, hasta *K, visitar func(clave K, dato V) bool) {
	if arbol.raiz == nil {
		return
	}
	if desde == nil {
		primerNodo := arbol.raiz.primero()
		desde = &primerNodo.clave
	}
	if hasta == nil {
		ultimoNodo := arbol.raiz.ultimo()
		hasta = &ultimoNodo.clave
	}
	arbol.raiz.iterarRango(desde, hasta, visitar, arbol.funcCmp)
}

func (nodo *nodoAbb[K, V]) iterarRango(desde *K, hasta *K, visitar func(clave K, dato V) bool, cmp func(K, K) int) bool {
	if nodo == nil {
		return true
	}

	if cmp(nodo.clave, *desde) < 0 {
		return nodo.der.iterarRango(desde, hasta, visitar, cmp)
	} else if cmp(nodo.clave, *hasta) > 0 {
		return nodo.izq.iterarRango(desde, hasta, visitar, cmp)
	} else if cmp(nodo.clave, *hasta) == 0 && cmp(nodo.clave, *desde) == 0 {
		visitar(nodo.clave, nodo.dato)
		return false
	}

	if !nodo.izq.iterarRango(desde, hasta, visitar, cmp) {
		return false
	}

	if !visitar(nodo.clave, nodo.dato) {
		return false
	}

	return nodo.der.iterarRango(desde, hasta, visitar, cmp)
}

func (arbol *abb[K, V]) Iterar(visitar func(clave K, dato V) bool) {
	arbol.IterarRango(nil, nil, visitar)
}

//--Iteradores Externos--

type iterExterno[K comparable, V any] struct {
	anteriores pila.Pila[*nodoAbb[K, V]]
	actual     *nodoAbb[K, V]
}

func (arbol *abb[K, V]) IteradorRango(desde *K, hasta *K) IterDiccionario[K, V] {
	newIter := new(iterExterno[K, V])
	newIter.anteriores = pila.CrearPilaDinamica[*nodoAbb[K, V]]()
	newIter.anteriores.Apilar(nil) // última vez que iteró

	if arbol.raiz != nil {
		if desde == nil {
			primerNodo := arbol.raiz.primero()
			desde = &primerNodo.clave
		}
		if hasta == nil {
			ultimoNodo := arbol.raiz.ultimo()
			hasta = &ultimoNodo.clave
		}

		arbol.raiz.apilarNodosPorRango(desde, hasta, newIter, arbol.funcCmp)
	}

	newIter.actual = newIter.anteriores.Desapilar() // primer elemento actual
	return newIter
}

func (nodo *nodoAbb[K, V]) apilarNodosPorRango(desde *K, hasta *K, iter *iterExterno[K, V], cmp func(K, K) int) {
	if nodo == nil {
		return
	}
	if iter.anteriores.VerTope() != nil {
		if cmp(iter.anteriores.VerTope().clave, *desde) <= 0 {
			return
		}
	}
	nodo.der.apilarNodosPorRango(desde, hasta, iter, cmp)
	if cmp(nodo.clave, *desde) >= 0 && cmp(nodo.clave, *hasta) <= 0 {
		iter.anteriores.Apilar(nodo)
	}
	nodo.izq.apilarNodosPorRango(desde, hasta, iter, cmp)

}

func (arbol *abb[K, V]) Iterador() IterDiccionario[K, V] {
	return arbol.IteradorRango(nil, nil)
}

func (iter *iterExterno[K, V]) HaySiguiente() bool {
	return iter.actual != nil
}

func (iter *iterExterno[K, V]) VerActual() (K, V) {
	iter.verificarIteracion()
	return iter.actual.clave, iter.actual.dato
}

func (iter *iterExterno[K, V]) Siguiente() {
	iter.verificarIteracion()
	iter.actual = iter.anteriores.Desapilar()
}

func (iter *iterExterno[K, V]) verificarIteracion() {
	if !iter.HaySiguiente() {
		panic("El iterador termino de iterar")
	}
}


func (arbol *abb[K, V]) RecorridoNivelesInverso() []K {
	res := []K{}
	pilaAux := pila.CrearPilaDinamica[K]()
	colaAux := cola.CrearColaEnlazada[*nodoAbb[K, V]]()
	act := arbol.raiz
	colaAux.Encolar(act)
	for ! colaAux.EstaVacia() {
		nodo := colaAux.Desencolar()
		if nodo.izq != nil {
			colaAux.Encolar(nodo.izq)
		} 
		if nodo.der != nil {
			colaAux.Encolar(nodo.der)
		}
		pilaAux.Apilar(nodo.clave)
	}
	for ! pilaAux.EstaVacia() {
		res = append(res, pilaAux.Desapilar())
	}
	return res
}