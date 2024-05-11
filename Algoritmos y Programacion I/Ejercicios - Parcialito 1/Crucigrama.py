def cruci(cruci):
	for t in cruci:
		if t[0] == 'BLANCA' and len(t[1])==0:
			return False
		if t[0] == 'NEGRA' and len(t[1])!=0:
			return False
		return True
