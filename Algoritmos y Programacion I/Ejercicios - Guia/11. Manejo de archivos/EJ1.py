def head(file, n):
	with open(file) as f:
		for n in range(n):
			for l in f:
				l = l.rstrip('\n')
				print(l)
				break


head('poema.txt', 5)


