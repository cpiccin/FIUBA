package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	archivo, err := os.Open("neruda.txt")
	if err != nil {
		fmt.Printf("Archivo %s no encontrado", "neruda.txt")
		return
	}
	defer archivo.Close()

	s := bufio.NewScanner(archivo)
	for s.Scan() {
		fmt.Printf("%s\n",s.Text())
	}
	err = s.Err()
	if err != nil {
		fmt.Println(err)
	}
}



