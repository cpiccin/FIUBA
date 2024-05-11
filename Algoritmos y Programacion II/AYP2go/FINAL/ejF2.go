// Implementar en Go una primitiva para el ABB que, dada una clave, nos devuelva una lista con todas las claves del
// árbol que sean mayores que la pasada por parámetro.


func (abb *abb[K, V]) clavesMayores(k K) []Lista {
	res = tda.CrearListaEnlazada[K]()
	return abb.clavesMayoresRec(abb.raiz, k, res)
}

func (abb *abb[K, V]) clavesMayoresRec(nodo *nodoAbb[K, V], k K, res []Lista) {
	if nodo == nil {
		return res 
	}
	if abb.funcCmp(nodo.clave, k) < 0 {
		abb.clavesMayoresRec(nodo.der, k, res)
	} else if abb.funcCmp(nodo.clave, k) > 0 {
		res.InsertarUltimo(nodo.clave)
		abb.clavesMayoresRec(nodo.izq, k, res)
		abb.clavesMayoresRec(nodo.der, k, res)
	}	
}
