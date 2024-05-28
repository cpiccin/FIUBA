trenDirecto(saarbruecken,dudweiler).
trenDirecto(forbach,saarbruecken).
trenDirecto(freyming,forbach).
trenDirecto(stAvold,freyming).
trenDirecto(fahlquemont,stAvold).
trenDirecto(metz,fahlquemont).
trenDirecto(nancy,metz).

/*Escribir un predicado viajar/2 (el /2 significa que recibe 2 parametros) que permita averiguar si es 
 * posible o no viajar de una localidad a otra, ya sea en uno o más tramos de tren. 
 * Por ejemplo, viajar(nancy,saarbruecken) debe dar verdadero.*/

viajar(X, Y) :- trenDirecto(X, Y).
viajar(X, Y) :- trenDirecto(X, Z), viajar(Z, Y).
