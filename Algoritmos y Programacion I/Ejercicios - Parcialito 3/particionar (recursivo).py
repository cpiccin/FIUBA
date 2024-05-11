def particionar(L, f):
	L_true, L_false = _particionar(L, f, [], [])
	return L_true + L_false

def _particionar(L, f, L_true, L_false):
	if len(L) == 0:
		return L_true, L_false
	if f(L[0]):
		L_true.append(L[0])
	else:
		L_false.append(L[0])
	return _particionar(L[1:], f, L_true, L_false)

def es_par(n):
    return n%2==0

print(particionar([7,8,3,5,2], es_par))


