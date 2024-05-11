package votos

import (
	"tdas/pila"
	"tp1/errores"
)

type votanteImplementacion struct {
	dni           int
	voto          Voto
	yaVoto        bool
	votosActuales pila.Pila[Voto]
}

func CrearVotante(dni int) Votante {
	nuevo := new(votanteImplementacion)
	nuevo.dni, nuevo.yaVoto, nuevo.votosActuales = dni, false, pila.CrearPilaDinamica[Voto]()
	nuevo.votosActuales.Apilar(nuevo.voto)
	return nuevo
}

func (votante votanteImplementacion) LeerDNI() int {
	return votante.dni
}

func (votante *votanteImplementacion) Votar(tipo TipoVoto, alternativa int) error {
	if votante.yaVoto == true {
		return errores.ErrorVotanteFraudulento{votante.dni}
	}
	if alternativa == 0 || votante.voto.VotoPorTipo[tipo] == -1 {
		alternativa = -1
		votante.voto.Impugnado = true
	}
	votante.voto.VotoPorTipo[tipo] = alternativa
	votante.votosActuales.Apilar(votante.voto)
	return nil
}

func (votante *votanteImplementacion) Deshacer() error {
	votante.votosActuales.Desapilar()
	if votante.yaVoto == true {
		return errores.ErrorVotanteFraudulento{votante.dni}
	}
	if votante.votosActuales.EstaVacia() {
		votante.votosActuales.Apilar(Voto{VotoPorTipo: [CANT_VOTACION]int{0, 0, 0}, Impugnado: false})
		return errores.ErrorNoHayVotosAnteriores{}
	}
	votante.voto = votante.votosActuales.VerTope() // vuelvo a la "version" anterior de los votos
	return nil
}

func (votante *votanteImplementacion) FinVoto() (Voto, error) {
	if votante.yaVoto == true {
		votante.voto.Impugnado = true
		return votante.voto, errores.ErrorVotanteFraudulento{votante.dni}
	}
	votante.yaVoto = true
	return votante.voto, nil
}
