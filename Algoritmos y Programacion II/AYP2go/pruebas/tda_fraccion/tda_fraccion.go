package fraccion
import "fmt"
type Fraccion struct {
	numerador int
	denominador int
	}

// CrearFraccion crea una fraccion con el numerador y denominador indicados. 
// Si el denominador es 0, entra en panico.
func CrearFraccion(numerador, denominador int) Fraccion {
	if denominador == 0 {
		panic("El denominador no puede ser 0")
	}
	return Fraccion{numerador, denominador}
}

// Sumar crea una nueva fraccion, con el resultante de hacer la suma de las fracciones originales
func (f Fraccion) Sumar(otra Fraccion) Fraccion {
	if f.denominador > otra.denominador {
		return Fraccion{f.numerador + otra.numerador, f.denominador}
	} else {
		return Fraccion{f.numerador + otra.numerador, otra.denominador}
	}
}

// Multiplicar crea una nueva fraccion con el resultante de multiplicar ambas fracciones originales
func (f Fraccion) Multiplicar(otra Fraccion) Fraccion {
	return Fraccion{f.numerador*otra.numerador,f.denominador*otra.denominador}
}

// ParteEntera devuelve la parte entera del numero representado por la fracción. 
// Por ejemplo, para "7/2" = 3.5 debe devolver 3. 
func (f Fraccion) ParteEntera() int {
	valor_fraccion := f.numerador/f.denominador
	return int(valor_fraccion)
}


// Representacion devuelve una representación en cadena de la fraccion simplificada (por ejemplo, no puede devolverse
// "10/8" sino que debe ser "5/4"). Considerar que si se trata de un número entero, debe mostrarse como tal.
// Considerar tambien el caso que se trate de un número negativo. 
func (f Fraccion) Representacion() string {
	x := f.denominador
	y := f.numerador
	mcm := Aux_Euclides(x, y)
	f.numerador = int(f.numerador/mcm)
	f.denominador = int(f.denominador/mcm)
	return fmt.Sprintf("%d", f.numerador, "/%d", f.denominador)
}

func Aux_Euclides(m int, n int) {
	var resto int
	for true {
		resto = m%n 
		if resto == 0 {
			return n
		}
		m = n 
		n = resto
	}
}

