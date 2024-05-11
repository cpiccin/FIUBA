def verifica(v1, v2):
	lista_v1 = v1.split('.')
	lista_v2 = v2.split('.')
	for i in range(3):
		if lista_v1[i] > lista_v2[i]:
			return 1
		if lista_v1[i] < lista_v2[i]:
			return -1
		if lista_v1[i] == lista_v2[i]:
			continue
	return 0


print(verifica('0.1.1','0.1.1'))