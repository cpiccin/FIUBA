package verificaciones


type ErrorComandoAgregarArchivo struct {}

func (e ErrorComandoAgregarArchivo) Error() string {
	return "Error en comando agregar_archivo"
}