def numeros_triangulares(n):
	num = 0
	for x in range(1, n+1):
		num += x
		print(f'{x} {num}') 



def numeros_triangulares2(n):
	num = 0
	for x in range(1, n+1):
		num = (x*(x+1))/2
		print(x, int(num))


