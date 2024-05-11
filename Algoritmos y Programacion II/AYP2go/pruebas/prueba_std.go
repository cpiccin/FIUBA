package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {
	scanner := bufio.NewScanner(os.Stdin) // inicio un scanner

	for scanner.Scan(){
		fmt.Print("> ")

		input := scanner.Text() // devuelve lo ultimo que leyo el scanner
		input = strings.TrimSpace(input) // saca espacios del final, es para algo de los comandos

		arr_input := strings.Split(input, " ") // separo en un array el input 

		comando := arr_input[0] // el primer elemento del array es el comando ingresado
		args := arr_input[1:] // los argumentos son todo lo que sigue en el array

		switch comando {

		case "saludar": // si el comando es saludar, saluda
			if len(args) < 1 {
				fmt.Fprintln(os.Stderr, "Falta un argumento para 'saludar'")
				continue
			}
			fmt.Fprintln(os.Stdout, "Hola!")
			
		case "emote": // si el comando es emote te responde segun lo que sea
			if len(args) < 1 {
				fmt.Fprintln(os.Stderr, "Falta un argumento para 'emote'")
				continue
			}
			switch args[0] {
			case ":)", ":D":
				fmt.Fprintln(os.Stdout, "Que bueno!")
			case ":(", ":'(":
				fmt.Fprintln(os.Stdout, "Que mal")
			default:
				fmt.Fprintln(os.Stdout, "No se que me queres decir")
			}
		case "chau": // terminas la conversacion con chau
			fmt.Fprintln(os.Stdout, "Chau!")
			return
		default:
			fmt.Fprintln(os.Stderr, "Comando indefinido: ", comando)
		}
	}
}
