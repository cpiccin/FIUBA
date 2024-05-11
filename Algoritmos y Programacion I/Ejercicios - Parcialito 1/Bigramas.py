def obtener_bigramas(texto):
    lista_texto = texto.split(' ')
    lista_final = []
    for i in range(len(lista_texto)):
        for p in lista_texto:
            lista_final.append((p[i], p[i]))
    return lista_final

print(obtener_bigramas("Uno se alegra de resultar útil"))