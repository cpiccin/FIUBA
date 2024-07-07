package votos

import (
	"fmt"
	"os"
)

type urnaImplementacion struct {
	votos      []Voto
	impugnados int
}

func CrearUrna() Urna {
	nueva := new(urnaImplementacion)
	nueva.impugnados = 0
	return nueva
}

func (urna *urnaImplementacion) IngresarVoto(voto Voto) {
	urna.votos = append(urna.votos, voto)
}

func (urna *urnaImplementacion) ConteoFinal(partidos []Partido) {
	for _, voto := range urna.votos {
		if voto.Impugnado == false {
			for i, alt := range voto.VotoPorTipo {
				partidos[alt].VotadoPara(TipoVoto(i))
			}
		} else if voto.Impugnado == true {
			urna.impugnados++
		}
	}
}

func (urna *urnaImplementacion) ImprimirResultados(partidos []Partido) {

	fmt.Fprintf(os.Stdout, "Presidente:\n")
	obtenerResultadoDelPartido(TipoVoto(0), partidos)

	fmt.Fprintf(os.Stdout, "\n")

	fmt.Fprintf(os.Stdout, "Gobernador:\n")
	obtenerResultadoDelPartido(TipoVoto(1), partidos)

	fmt.Fprintf(os.Stdout, "\n")

	fmt.Fprintf(os.Stdout, "Intendente:\n")
	obtenerResultadoDelPartido(TipoVoto(2), partidos)

	fmt.Fprintf(os.Stdout, "\n")

	if urna.impugnados == 1 {
		fmt.Fprintf(os.Stdout, "Votos Impugnados: %d voto", urna.impugnados)
	} else {
		fmt.Fprintf(os.Stdout, "Votos Impugnados: %d votos", urna.impugnados)
	}
	fmt.Println()
}

func obtenerResultadoDelPartido(tipo TipoVoto, partidos []Partido) {
	for i := 0; i < len(partidos); i++ {
		fmt.Fprintf(os.Stdout, "%s\n", partidos[i].ObtenerResultado(tipo))
	}
}
