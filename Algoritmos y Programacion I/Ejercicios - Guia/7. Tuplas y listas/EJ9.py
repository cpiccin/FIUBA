def empaquetar2(lista):
    lista_final = []
    contador = 1
    if lista == []: #caso borde lista vacia (se rompe en el for)
        return lista
    if len(lista) == 1: #caso borde lista de un solo elemento (se rompe en el for)
        lista_final.append((lista[0], contador))
        return lista_final
    for x in range(len(lista)-1): #para que no tire indexerror
        if lista[x] == lista[x+1]: #si a la posicion x le sigue uno igual...
            if x != (len(lista)-2): #y a su vez x no corresponde a la anteultima posicion...
                contador += 1
            else: #y a su vez x corresponde a la anteultima posicion... (significa que queda un numero igual por delante que sera el ultimo de la lista)
                contador += 1
                lista_final.append((lista[x], contador))
        else: #si a la posicion x no le sigue ninguno igual...
            lista_final.append((lista[x], contador))
            contador = 1 #el contador vuelve a 1 para la siguiente tupla
    if lista_final[len(lista_final)-1] != (lista[len(lista)-1], contador):
        lista_final.append((lista[len(lista)-1], contador))
    return lista_final

print(empaquetar2([1,1,1,1,1,2,3,4,4,4,45,5,5,6,6,7,5,3,43,4,34,3,4,3,2,2]))