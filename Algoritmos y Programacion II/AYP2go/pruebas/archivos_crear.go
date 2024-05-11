package main

import (
	"bufio"
	"fmt"
	"os"
)

const ruta = "neruda_2.0.txt"

func main() {
	file, err := os.Create(ruta)
	if err != nil {
		fmt.Printf("No se pudo crear el archivo %s", ruta)
		return
	}
	defer file.Close()

	datawriter := bufio.NewWriter(file)

	for _, dato := range []string{"hola", "Holanda", "EE.UU"} {
		_, err = datawriter.WriteString(dato + "\n")
		if err != nil {
			fmt.Printf("No se pudo guardar la linea %s, error: %v", dato, err)
		}
	}
	datawriter.Flush()
}