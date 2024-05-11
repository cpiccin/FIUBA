def total_por_local(vendedores, locales):
	res = {}
    for local, vendedores_local in locales.items():
        res[local] = res.get(local, 0)
        for vendedor in vendedores:
            if vendedor in vendedores_local:
                res[local] += vendedores[vendedor]
                continue
    return res 


dic1 = {'Pepe':2323,'Luciana':3222,'Marta':6776, 'Cacho':3551, 'Hugo':9983,'Ana':1245, 'Rober':4463}
dic2 = {'Carrefour': ['Luciana', 'Cacho', 'Hugo'], 'Dia%': ['Pepe', 'Marta', 'Ana'], 'Maxigomez': ['Rober', 'Chacho']}


print(total_por_local(dic1, dic2))