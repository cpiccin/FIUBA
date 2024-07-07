package complejo

import (
	"math"
	"fmt"
)


type Complejo struct {
	real float64
	img  float64
}

func CrearComplejo(real float64, img float64) *Complejo {
	return &Complejo{real: real, img: img}
}

func (comp *Complejo) Multiplicar(otro *Complejo) {
	parteReal := (comp.real)*(otro.real) - (comp.img)*(otro.img)
	parteImg := (comp.img)*(otro.real) + (comp.real)*(otro.img)
	comp.real, comp.img = parteReal, parteImg
}

func (comp *Complejo) Sumar(otro *Complejo) {
	parteReal := comp.real + otro.real
	parteImg := comp.img + otro.img
	comp.real, comp.img = parteReal, parteImg
}

func (comp *Complejo) ParteReal() float64 {
	return comp.real
}

func (comp *Complejo) ParteImaginaria() float64 {
	return comp.img
}

func (comp *Complejo) Modulo() float64 {
	n := (comp.real)*(comp.real) + (comp.img)*(comp.img)
	return math.Sqrt(n)
}

func (comp *Complejo) Angulo() float64 {
	n := (comp.img) / (comp.real)
	return math.Atan(n)
}

func PrintComplejo(n *Complejo) {
	fmt.Printf("%f + i%f", n.ParteReal(), n.ParteImaginaria())
}