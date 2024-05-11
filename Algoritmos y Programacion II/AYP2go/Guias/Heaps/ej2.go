// Implementar una primitiva para el heap (de máximos) que obtenga los 3 elementos más grandes del heap en O(1).

func (h heap[T]) Max3() []T {
	res := []T{}
	for i := 0; i < 3 && i < h.cantidad; i++ {
		res = append(res, h.datos[i])
	}
	if len(res) == 3 && h.cmp(res[1], res[2]) < 0 {
		res[1], res[2] = res[2], res[1]
	}
	return res
}