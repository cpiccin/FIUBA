def num_im(t):
	if t[0]!=0 and t[1]!=0 and t[1]>0:
		return (str(t[0]) + '+' + str(t[1]) + 'i')
	if t[0]!=0 and t[1]!=0 and t[1]<0:
		return (str(t[0]) + str(t[1]) + 'i')
	if t[0]!=0 and t[1]==0:
		return str(t[0])
	if t[1]!=0 and t[0]==0:
		return (str(t[1])+'i')


print(num_im((3, 6)))
print(num_im((5,0)))
print(num_im((1, -2)))
print(num_im((0, -4)))

