def ajedrez(n):
	for i in range(n):
		for j in range(n):
			if (i+j)%2==0 :
				print('B', end=' ')
			else:
				print('n', end=' ')
		print()


ajedrez(4)