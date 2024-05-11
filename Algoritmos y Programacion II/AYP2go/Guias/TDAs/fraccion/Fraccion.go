package fraccion

type Frac interface {
	CrearFraccion(n, d int) Fraccion
	Sumar(Fraccion) Fraccion 
	Multiplicar(Fraccion) Fraccion
	ParteEntera() int 
	Representacion() string
}