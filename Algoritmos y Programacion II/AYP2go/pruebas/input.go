package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	fmt.Println("Ingrese de a uno, linea vacia para terminar. ")
	s := bufio.NewScanner(os.Stdin)
	numbers := ""
	for s.Scan() {
		if s.Text() == "" {
			break
		}
		numbers = numbers + s.Text() + " "
	}
	err := s.Err()
	if err != nil {
		fmt.Println(err)
	}
	fmt.Println(numbers)
}


