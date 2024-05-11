package votos

import "fmt"

type partidoImplementacion struct {
	nombre     string
	candidatos []string
	votos      []int
}

type partidoEnBlanco struct {
	votos []int
}

func CrearPartido(nombre string, candidatos [CANT_VOTACION]string) Partido {
	partido := new(partidoImplementacion)
	partido.nombre = nombre
	partido.candidatos = []string{candidatos[0], candidatos[1], candidatos[2]}
	partido.votos = []int{0, 0, 0}
	return partido
}

func CrearVotosEnBlanco() Partido {
	nuevo := new(partidoEnBlanco)
	nuevo.votos = []int{0, 0, 0}
	return nuevo
}

func (partido *partidoImplementacion) VotadoPara(tipo TipoVoto) {
	partido.votos[tipo]++
}

func (partido partidoImplementacion) ObtenerResultado(tipo TipoVoto) string {
	if partido.votos[tipo] == 1 {
		return fmt.Sprintf("%s - %s: %d voto", partido.nombre, partido.candidatos[tipo], partido.votos[tipo])
	}
	return fmt.Sprintf("%s - %s: %d votos", partido.nombre, partido.candidatos[tipo], partido.votos[tipo])
}

func (blanco *partidoEnBlanco) VotadoPara(tipo TipoVoto) {
	blanco.votos[tipo]++
}

func (blanco partidoEnBlanco) ObtenerResultado(tipo TipoVoto) string {
	if blanco.votos[tipo] == 1 {
		return fmt.Sprintf("Votos en Blanco: %d voto", blanco.votos[tipo])
	}
	return fmt.Sprintf("Votos en Blanco: %d votos", blanco.votos[tipo])
}
