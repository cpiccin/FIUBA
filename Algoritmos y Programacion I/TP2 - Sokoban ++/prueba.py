def agrega_espacios(desc):
    max_len = 0
    for linea in desc:
        if max_len < len(linea):
            max_len = len(linea)
        
    for i in range(len(desc)):
        if len(desc[i]) < max_len:
            desc[i] += '#'*(max_len-len(desc[i]))
    
    return desc
    
desc = ['1234', '12', '123456', '123', '1234']
print(agrega_espacios(desc))