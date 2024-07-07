package auxiliares

import "tp1/votos"

func RadixSort(padrones []votos.Votante) []votos.Votante {

	cant := len(padrones)
	ordenados := make([]votos.Votante, cant)

	for cifra := 1; cifra <= 10000000; cifra *= 10 {
		count := [10]int{}

		for i := 0; i < cant; i++ {
			count[(padrones[i].LeerDNI()/cifra)%10]++
		}

		for i := 1; i < 10; i++ {
			count[i] += count[i-1]
		}

		for i := cant - 1; i >= 0; i-- {
			countIndex := (padrones[i].LeerDNI() / cifra) % 10
			count[countIndex]--
			ordenados[count[countIndex]] = padrones[i]
		}

		for i := 0; i < cant; i++ {
			padrones[i] = ordenados[i]
		}
	}

	return padrones
}
