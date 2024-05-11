movimientos = [("Pikachu", "Impactrueno"), ("Charizard", "Lanzallamas"),
               ("Pikachu", "Ataque Rápido"), ("Charizard", "Lanzallamas")]


def movimientos_notables(lista, k):
    dic = {}
    for tupla in lista:
        if tupla in dic:
            dic[tupla] += 1
            continue
        dic[tupla] = dic.get(tupla, 1)

    veces = k
    quien = None

    for clave in dic:
        if dic[clave] > veces:
            veces = dic[clave]
            quien = clave


    print(f'{quien[0]} - {quien[1]} ({veces})')



movimientos_notables(movimientos, 1)

