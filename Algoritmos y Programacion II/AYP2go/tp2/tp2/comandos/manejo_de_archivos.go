package comandos


import (
	"os"
	"fmt"
	"bufio"
	"strings"
	v "tp2/vuelos"
	dicc "tdas/diccionario"
	verifica "tp2/verificaciones"
)


func agregarArchivo(archivos []string, prioridad dicc.Diccionario[string, int], almacenaVuelos dicc.Diccionario[string, v.InfoVuelos]) {
	fileVuelos, err := os.Open(archivos[0])
	if ! verifica.VerificaArchivoValido(err) {
		return
	}
	procesarArchivo(fileVuelos, prioridad, almacenaVuelos)
	fileVuelos.Close()
	fmt.Fprintf(os.Stdout, "OK\n")
}

func procesarArchivo(file *os.File, prioridad dicc.Diccionario[string, int], hashVuelos dicc.Diccionario[string, v.InfoVuelos]) {
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		infoVuelo := strings.Split(strings.TrimSpace(scanner.Text()), ",")
		nuevoVuelo := v.CrearVuelo(infoVuelo)
		prioridad.Guardar(nuevoVuelo.Codigo(),nuevoVuelo.Prioridad())
		hashVuelos.Guardar(nuevoVuelo.Codigo(), nuevoVuelo)
		
	}
}
