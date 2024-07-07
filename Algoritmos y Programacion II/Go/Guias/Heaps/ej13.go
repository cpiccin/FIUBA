package main 
import(
    "fmt"
    tda "tdas/cola_prioridad"
)

func main() {
    arr := []int{11, 14, 8, 19, 42, 3, 1, 9}
    fmt.Println(Combinar(arr, 13))
    fmt.Println(arr)
}

func Combinar(arr []int, k int) []int {
    res := []int{}
    heapAux := tda.CrearHeap[int](funcMin)
    for i := range arr {
        if arr[i] < k {
            heapAux.Encolar(arr[i])
        } else {
            res = append(res, arr[i])
        }
    }
    for ! heapAux.EstaVacia() {
        primero := heapAux.Desencolar()
        if heapAux.EstaVacia() {
            return nil
        }
        segundo := heapAux.Desencolar()
        n := primero + 2*segundo
        if n > k {
            res = append(res, n)
        } else if n < k {
            heapAux.Encolar(n)
        }
    }
    return res
}
func funcMin(n1, n2 int) int {
    if n1 < n2 {
        return 1
    } else if n2 > n1 {
        return -1
    }
    return 0
}