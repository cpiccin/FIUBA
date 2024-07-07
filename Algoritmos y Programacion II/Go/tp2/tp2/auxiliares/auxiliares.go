package auxiliares

import (
	"strconv"
	"strings"
	v "tp2/vuelos"
)

// -- Funciones de Comparacion -- //

func FuncCmpHeapPrioridades(vuelo1, vuelo2 v.Vuelo) int {
	if vuelo1.Prioridad() > vuelo2.Prioridad() {
		return 1
	}
	if vuelo1.Prioridad() < vuelo2.Prioridad() {
		return -1
	}
	return funcCmpCodigo(vuelo1.Codigo(), vuelo2.Codigo())
}

func FuncCmpHeapFechaDesc(vuelo1, vuelo2 v.Vuelo) int {
	resDesc := FuncCmpHeapFechaAsc(vuelo1, vuelo2)
	return resDesc * (-1)
}

func FuncCmpHeapFechaAsc(vuelo1, vuelo2 v.Vuelo) int {
	fecha1, _ := FechaAInt(vuelo1.Fecha())
	fecha2, _ := FechaAInt(vuelo2.Fecha())
	if fecha1 < fecha2 {
		return -1
	}
	if fecha1 > fecha2 {
		return 1
	}
	return funcCmpCodigo(vuelo1.Codigo(), vuelo2.Codigo())
}

func FuncCmpAbbFechaAsc(fecha1, fecha2 int) int {
	if fecha1 < fecha2 {
		return -1
	}
	if fecha1 > fecha2 {
		return 1
	}
	return 0
}

func FuncCmpAbbFechaDesc(fecha1, fecha2 int) int {
	resDesc := FuncCmpAbbFechaAsc(fecha1, fecha2)
	return resDesc * (-1)
}

func funcCmpCodigo(codigo1, codigo2 string) int {
	if codigo1 < codigo2 {
		return 1
	}
	if codigo1 > codigo2 {
		return -1
	}
	return 0
}

// -- Auxiliares -- //

func FechaAInt(s string) (int, error) {
	cadFecha := strings.Split(s, "T")
	dia, hora := strings.Split(cadFecha[0], "-"), strings.Split(cadFecha[1], ":")
	cadRes := strings.Join(dia, "") + strings.Join(hora, "")
	res, err := strconv.Atoi(cadRes)
	return res, err
}
