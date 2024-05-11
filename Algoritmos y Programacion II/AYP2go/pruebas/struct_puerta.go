package main 
import "fmt"

func main() {
	var puerta1 Puerta 
	fmt.Println(puerta1.estado)
	fmt.Println(puerta1.estaAbierta())
	puerta1.abrir()
	fmt.Println(puerta1.estaAbierta())
}


type Puerta struct {
	estado bool;
}

func (puerta *Puerta) cerrar() {
	puerta.estado = false;
}

func (puerta *Puerta) abrir() {
	puerta.estado = true;
}

func (puerta *Puerta) estaAbierta() (string){
	if puerta.estado == true {
		return "La puerta esta abierta"
	}
	return "La puerta esta cerrada"
}