// Implementar una función func balanceado(texto string) boolean, que retorne si texto esta balanceado o no.El texto sólo
// puede contener los siguientes caracteres: [,],{,}(,). Indicar y justificar la complejidad de la función implementada.
// Un texto esta balanceado si cada agrupador abre y cierra en un orden correcto. Por ejemplo:
		// balanceado("[{([])}]") => true
		// balanceado("[{}") => false
		// balanceado("[(])") => false
		// balanceado("()[{}]") => true
		// balanceado("()()(())") => true

package main 

import (
	"fmt"
	tda "tdas/pila"
)

func main() {

}

func balanceado(texto string) bool {
	pilaAux := tda.CrearPilaDinamica[string]()
	for i := 0; i < len(texto); i++ {
		char := string(texto[i])
		if pilaAux.EstaVacia() {
			pilaAux.Apilar(char)
		} else if char == "[" || char == "{" || char == "(" {
			pilaAux.Apilar(char)
		} else if char == "]" && pilaAux.VerTope() == "[" {
			pilaAux.Desapilar()
		} else if char == "}" && pilaAux.VerTope() == "{" {
			pilaAux.Desapilar()
		} else if char == ")" && pilaAux.VerTope() == "(" {
			pilaAux.Desapilar()
		} else {
			continue
		}
	}
	if pilaAux.EstaVacia() {
		return true
	}
	return false
}