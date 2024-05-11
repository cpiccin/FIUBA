def es_primo(n):
    for x in range(2, n):
        if n%x == 0:
            return False
    return True
    
def siguiente_primo(n):
    while True:
        n += 1
        if es_primo(n)==True:
            break
    return n

def descompone_en_primos(k):
    divisor = 2
    while k > 1:
        if k % divisor == 0:
            k //= divisor
            print(divisor)
        else:
            divisor = siguiente_primo(divisor)
    
    
            