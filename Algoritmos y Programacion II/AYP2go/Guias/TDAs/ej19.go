package main 

import ( 
    "fmt"
    TDAPila "TDAs/pila")

func main() {
    a := "[{([])}]"
    b := "[{}"
    c := "[(])"
    d := "()[{}]"
    e := "()()(())"
    fmt.Println(Balanceado(a))
    fmt.Println(Balanceado(b))
    fmt.Println(Balanceado(c))
    fmt.Println(Balanceado(d))
    fmt.Println(Balanceado(e))
}


func Balanceado(texto string) bool {
    pila_aux := TDAPila.CrearPilaDinamica[string]()
    for i := range texto {
        elem := string(texto[i])

        if pila_aux.EstaVacia() {
            pila_aux.Apilar(elem)
        } else if elem == "[" || elem == "{" || elem == "(" {
            pila_aux.Apilar(elem)
        } else if pila_aux.VerTope() == "[" && elem == "]" {
            pila_aux.Desapilar()
        } else if pila_aux.VerTope() == "{" && elem == "}" {
            pila_aux.Desapilar()
        } else if pila_aux.VerTope() == "(" && elem == ")" {
            pila_aux.Desapilar()
        } else {
            continue
        }
    }
    if pila_aux.EstaVacia() {
        return true
    }
    return false
}