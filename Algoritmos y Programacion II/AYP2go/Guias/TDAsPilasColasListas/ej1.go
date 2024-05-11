package fraccion

import "fmt"

type Fraccion struct {
	numerador int
	denominador int 
}

func CrearFraccion(n, d int) Fraccion {
	validaDenominador(d)
	nueva_fraccion := Fraccion{}	
	nueva_fraccion.numerador, nueva_fraccion.denominador = n, d
	return nueva_fraccion 
}

func (f Fraccion) Sumar(otra Fraccion) Fraccion {
	f.simplifica()
	otra.simplifica()
	nueva_fraccion := CrearFraccion(f.numerador*otra.denominador + f.denominador*otra.numerador, f.denominador*otra.denominador)
	nueva_fraccion.simplifica()
	return nueva_fraccion
}

func (f Fraccion) Multiplicar(otra Fraccion) Fraccion {
	nueva_fraccion := CrearFraccion(f.numerador*otra.numerador, f.denominador*otra.denominador)
	nueva_fraccion.simplifica()
	return nueva_fraccion
}

func (f Fraccion) ParteEntera() int {
	n := f.numerador/f.denominador
	return n
}

func (f Fraccion) Representacion() string {
	f.simplifica()
	rep := fmt.Sprintf("%d/%d",f.numerador, f.denominador)
	if f.denominador == 1 {
		return fmt.Sprintf("%d", f.numerador)
	}
	return rep
}

func (f *Fraccion)simplifica() {
	mcd := euclides(f.numerador, f.denominador)
	f.numerador = f.numerador/mcd
	f.denominador = f.denominador/mcd
}

func euclides(m, n int) int {
	for true {
		resto := m % n
		if resto == 0 {
			return n 
		}
		m = n 
		n = resto
	}
	return 0
}

func validaDenominador(denominador int) {
	if denominador == 0 {
		panic("No se puede dividir por 0")
	}
}