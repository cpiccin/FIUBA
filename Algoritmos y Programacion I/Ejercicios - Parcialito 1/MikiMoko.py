def mikimoko():
    for n in range(1, 101):
        if n % 3 == 0 and n % 5 == 0:
            print('MikiMoko')
            continue
        if n % 3 == 0:
            print('Miki')
            continue
        if n % 5 == 0:
            print('Moko')
            continue
        print(n)
        

mikimoko()