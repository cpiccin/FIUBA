package auxiliares

import "tp1/votos"

func BusquedaBinaria(padrones []votos.Votante, dni, izq, der int) int {
	if izq > der {
		return -1
	}
	medio := (izq + der) / 2
	elemMedio := padrones[medio].LeerDNI()
	if elemMedio == dni {
		return medio
	}
	if dni < elemMedio {
		der = medio - 1
	} else {
		izq = medio + 1
	}
	return BusquedaBinaria(padrones, dni, izq, der)
}
