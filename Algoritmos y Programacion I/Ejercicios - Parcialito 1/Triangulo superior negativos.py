def cant_negativos_triangulo_sup(matriz):
    '''Dada una matriz cuadrada, devuelve la cantidad de numeros negativos que se encuentran en el triangulo superior de la matriz'''
    contador = 0
    lista_numeros_en_triangulo_sup = []
    for i in range(len(matriz[0])):
        for j in range(i, len(matriz[0])):
            lista_numeros_en_triangulo_sup.append(matriz[i][j])
    for n in lista_numeros_en_triangulo_sup:
        if n < 0:
            contador += 1
    return contador