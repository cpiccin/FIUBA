from string import ascii_lowercase

def rot13(archivo_origen, archivo_destino):
    '''Cifra cada linea de archivo_origen y la guarda en archivo_destino'''
    with open(archivo_origen, 'r') as archivo_origen, open(archivo_destino, 'w') as archivo_destino:
        
        for linea in archivo_origen:
            linea_cifrada = ''
            
            for c in linea:
                if c.isalpha():
                    pos = (ascii_lowercase.find(c)+13)%26
                    linea_cifrada += ascii_lowercase[pos]
                    continue
                linea_cifrada += c

            archivo_destino.write(linea_cifrada)


        