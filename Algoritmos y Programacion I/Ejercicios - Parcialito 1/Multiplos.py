def main():
    '''Pide dos numeros a y b e imprime los primeros a multiplos de b'''
    entrada_a = input("Ingrese el número 'a': ")
    while entrada_a.isdigit() == False or int(entrada_a) <= 0:
        entrada_a = input("Ingrese el número 'a': ")

    entrada_b = input("Ingrese el número 'b': ")
    while entrada_b.isdigit() == False or int(entrada_b) <= 0:
        entrada_b = input("Ingrese el número 'b': ") 

    entrada_a, entrada_b = int(entrada_a), int(entrada_b)
    for i in range(1, entrada_a+1):
        print(entrada_b*i)


main()