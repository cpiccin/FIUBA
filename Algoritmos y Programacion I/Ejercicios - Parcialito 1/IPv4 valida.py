def ip_valida():
    while True:
        entrada = input('Ingrese una IPv4: ')
        lista_entrada = entrada.split('.')
        if len(lista_entrada) != 4:
            continue
        for e in lista_entrada:
            if not 0<=int(e)<=255 or e.isdigit()!=True:
                break
            return '.'.join(lista_entrada)   
        continue
        


print(ip_valida())