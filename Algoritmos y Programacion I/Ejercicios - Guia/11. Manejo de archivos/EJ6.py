def cargar_datos(nombre_archivo):
    dic = {}
    with open(nombre_archivo, 'r') as nombre_archivo:
        
        for linea in nombre_archivo:
            linea = linea.split(',')
            if linea[0] in dic:
                dic[linea[0]].append(linea[1].rstrip())
                continue 
            dic[linea[0]] = [linea[1].rstrip()]
    
    return dic

datos = cargar_datos('original.txt')

def guardar_datos(datos, nombre_archivo):

    with open(nombre_archivo, 'w') as nombre_archivo:
        for clave, valor in datos.items():
            if len(valor)>1:
                for i in range(len(valor)):
                    nombre_archivo.write(f'{clave},{valor[i]}\n')
                continue
            valor = ''.join(valor)
            nombre_archivo.write(f'{clave},{valor}\n')


guardar_datos(datos, 'llegada.txt')