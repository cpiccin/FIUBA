def main():

	a = input('Ingrese a: ')
	while a.isdigit()!=True or int(float(a))!=float(a):
		a = input('Ingrese a: ')
	a = int(a)

	b = input('Ingrese b: ')
	while b.isdigit()!=True or int(float(b))!=float(b):
		b = input('Ingrese b: ')
	b = int(b)

	lista_pares = []
	for n in range(a, b+1):
		if n%2==0:
			lista_pares.append(n)

	return lista_pares



print(main())