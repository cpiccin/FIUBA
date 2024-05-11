def generador(n):
	res = []
	res.append(int(-n))
	n = int(-n)
	return _generador(n, res)

def _generador(n, L):
	if int(-n) == L[0]:
		return L 
	L.append(n+1)
	n = n+1 
	return _generador(n, L)


print(generador(2))
