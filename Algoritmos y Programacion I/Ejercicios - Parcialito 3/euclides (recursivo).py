def euclides(a, b):
	if a > b:
		res = (a%b)
		if res == 0:
			return b
		return euclides(b, res)
	if b > a:
		res = (b%a)
		if res == 0:
			return a
		return euclides(a, res)


print(euclides(20, 15))
print(euclides(12, 6))
print(euclides(32333, 30))