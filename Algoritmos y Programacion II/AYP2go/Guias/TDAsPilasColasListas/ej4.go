package ComposicionFunciones

import (
	"fmt"
	TDAPila "TDAs/pila"
)

type ComposicionFunciones struct {
	comp TDAPila.Pila[func(float64) float64]
	cantidad int
}

func CrearComposicion() ComposicionFunciones {
	nueva_comp := ComposicionFunciones{}
	nueva_comp.comp = TDAPila.CrearPilaDinamica[func(float64) float64]()
	return nueva_comp
}

func (comp ComposicionFunciones) AgregarFuncion(f func(float64) float64) {
	(comp.comp).Apilar(f)
	comp.cantidad++
}

func (comp ComposicionFunciones) Aplicar(x float64) float64 {
	copia := ComposicionFunciones{}
	copia.comp = TDAPila.CrearPilaDinamica[func(float64) float64]()

	for ! comp.comp.EstaVacia() {
		copia.comp.Apilar(comp.comp.VerTope())
		x = (comp.comp.Desapilar())(x)
		fmt.Println(x)
	}

	for ! copia.comp.EstaVacia() {
		comp.comp.Apilar(copia.comp.Desapilar())
	}

	return x
}


