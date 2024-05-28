
/*Escribir el predicado palindromo(Lista) que determine si la lista es palindrómica. 
 * Por ejemplo: palindromo([n,e,u,q,u,e,n]) debe dar verdadero.*/

palindromo(L) :- 
    reverse(L, ListaInvertida),
    ListaInvertida == L.
