def suma_digital(n):
    if n == 0:
        return n
    return n%10 + suma_digital(n//10)%10
    
    
print(suma_digital(2019))