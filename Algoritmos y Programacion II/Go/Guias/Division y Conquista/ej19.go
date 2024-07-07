// Se sabe, por el teorema de Bolsano, que si una función es continua en un intervalo [a, b], y que en el punto a es positiva y en el punto
// b es negativa (o viceversa), necesariamente debe haber (al menos) una raíz en dicho intervalo. 
// Implementar una función func raiz(f func(int)int, a int, b int) int que reciba una función (univariable) y los extremos mencionados 
// y devuelva una raíz dentro de dicho intervalo (si hay más de una, simplemente quedarse con una). La complejidad de dicha función debe
// ser logarítmica del largo del intervalo [a, b]. Asumir que por más que se esté trabajando con números enteros, hay raíz en dichos 
// valores: Se puede trabajar con floats, y el algoritmo será equivalente, simplemente se plantea con ints para no generar confusiones 
// con la complejidad. Justificar la complejidad de la función implementada.

package main

import "fmt"

