# a) Calcula perimetro de un rectangulo dada su base y altura

def perimetro_rectangulo(base, altura):
	perimetro = base * 2 + altura * 2
	return perimetro


# b) Calcula area de un rectangulo dada su base y altura

def area_rectangulo(base, altura):
	area = base * altura
	return area 


# c) Calcula area de un rectangulo dadas sus coordenadas x1, x2, y1, y2

def area_rectangulo_ejes(x1, x2, y1, y2):
	area = (x2 - x1) * (y2 - y1)
	return area 


# d) Calcula el perimetro de un circulo dado su radio (2pi*r)
from math import pi

def perimetro_circulo(r):
	perimetro = 2 * pi * r
	return perimetro


# e) Calcular area de un circulo dado su radio (pi*r^2)

def area_circulo(r):
	area = pi * (r**2)
	return area


# f) Calcula el volumen de una esfera dado su radio (4/3 pi * r^3)

def volumen_esfera(r):
	volumen = ((4/3)*pi) * (r**3)
	return volumen 


# g) Calcula la hipotenusa de un triangulo rectangulo, dados sus catetos (sqrt(c1^2 + c2^2))
 
def hipotenusa(c1, c2):
	hipotenusa = (c1**2 + c2**2)**(1/2)
	return hipotenusa
