package comandos

import "fmt"

type ErrorComando struct{}

func (e ErrorComando) Error(comando string) string {
	return fmt.Sprintf("Error en comando %s", comando)
}