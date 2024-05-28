
/*Una lista es duplicada si está compuesta por dos bloques consecutivos de los mismos 
 * elementos. Por ejemplo [a,b,c,a,b,c] es duplicada. 
 * Escribir un predicado duplicada(Lista) que determine si la lista es duplicada o no.*/


lista_duplicada(List) :- 
    append(Left, Right, List),
    Left = Right.
