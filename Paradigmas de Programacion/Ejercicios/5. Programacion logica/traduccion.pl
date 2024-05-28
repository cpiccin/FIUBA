traduccion(eins,uno).
traduccion(zwei,dos).
traduccion(drei,tres).
traduccion(vier,cuatro).
traduccion(fuenf,cinco).
traduccion(sechs,seis).
traduccion(sieben,siete).
traduccion(acht,ocho).
traduccion(neun,nueve).

/* Escribir el predicado traduccionLista(A,E) que produzca la traducción de una 
 * lista de números entre alemán y español.*/

traduccionLista([],[]). /*caso base lista vacia */
traduccionLista([H|Hs], [T|Ts]) :- 
    traduccion(H,T),
    traduccionLista(Hs, Ts).
    
