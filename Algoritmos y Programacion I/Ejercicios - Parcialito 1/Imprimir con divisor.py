def cada_n_lugares():
    n = input('Ingrese una frecuencia: ')
    while n.isdigit() != True or int(n)<=0: #caso borde donde no se ingreso un numero natural positivo
        n = input('Ingrese una frecuencia: ')
    n = int(n)
    frase = input('Ingrese una frase: ')
    cadena_final = ''
    for x in range(len(frase)): #suma caracter a caracter
        if x%n == 0 and x != 0:
            cadena_final += '-' + frase[x]
            continue
        cadena_final += frase[x]
    print(cadena_final)


cada_n_lugares()