// Es el año 1700, y la pirata Barba-ra Verde atacó un barco de la Royal British Shipping & Something, que transportaba una
// importante piedra preciosa de la corona británica. Al parecer, la escondieron en un cofre con muchas piedras preciosas falsas, en
// caso de un ataque. Barba-ra Verde sabe que los refuerzos británicos no tardarán en llegar, y deben uir lo más rápido posible. 
// El problema es que no pueden llevarse el cofre completo por pesar demasiado. Necesita encontrar rápidamente la joya verdadera.
// La única forma de descubrir la joya verdadera es pesando. Se sabe que la joya verdadera va a pesar más que las imitaciones, y
// que las imitaciones pesan todas lo mismo. Cuenta con una balanza de platillos para poder pesarlas (es el 1700, no esperen una
// balanza digital).

// a. Escribir un algoritmo de división y conquista, para determinar cuál es la verdadera joya de la corona. Suponer que hay una
// función balanza(grupo_de_joyas1, grupo_de_joyas2) que devuelve 0 si ambos grupos pesan lo mismo, mayor a 0 si el grupo1 pesa más
// que el grupo2, y menor que 0 si pasa lo contrario, y realiza esto en tiempo constante. b. Indicar y justificar (adecuadamente) 
// la complejidad de la función implementada.
package main

import "fmt"

func main() {
	arr := []int{2,2,3,2,2,2,2,2,2}
	fmt.Println(JoyaVerdadera(arr))
}

func JoyaVerdadera(joyas []int) int {
	return aux(joyas, 0, len(joyas)-1)
}

func aux(arr []int, ini, fin int) int {
	if (fin - ini) >= 1 && (fin - ini) <= 2 {
		return masPesada(arr, ini, fin)
	}
	medio := (fin+ini)/2
	grupo1, grupo2 := arr[ini:medio+1], arr[medio+1:fin+1]

	if len(grupo1) > len(grupo2) {
		if grupo1[len(grupo1)-1] > grupo1[len(grupo1)-2] {
			return grupo1[len(grupo1)-1]
		}
		grupo1 = grupo1[:len(grupo1)-1]
	}

	if len(grupo2) > len(grupo1) {
		if grupo2[len(grupo2)-1] > grupo2[len(grupo2)-2] {
			return grupo2[len(grupo2)-1]
		}
		grupo2 = grupo2[:len(grupo2)-1]
	}
	
	if balanza(grupo1, grupo2) > 0 {
		return aux(arr, ini, medio)
	} else if balanza(grupo1, grupo2) < 0 {
		return aux(arr, medio+1, fin)
	}
	return -1
}

func masPesada(arr []int, ini, fin int) int {
	res := 0 
	for i := ini; i <= fin; i++ {
		if arr[i] > res {
			res = arr[i]
		}
	}
	return res 
}

func balanza(g1, g2 []int) int {
	peso1, peso2 := 0, 0
	for i := 0; i < len(g1); i++ {
		peso1 += g1[i]
	}
	for j := 0; j < len(g2); j++ {
		peso2 += g2[j]
	}
	if peso1 == peso2 {
		return 0
	} else if peso1 > peso2 {
		return 1 
	} else {
		return -1
	}
}