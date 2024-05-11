def invertir_palabras(frase):
    '''Recibe una cadena que contiene palabras separadas por espacios y devuelve una nueva cadena con las letras de cada palabra invertidas'''
    lista_frase = frase.split()
    lista_final = []
    for p in lista_frase:
        lista_final.append(p[::-1])
    cadena_final = ' '.join(lista_final)
    return cadena_final