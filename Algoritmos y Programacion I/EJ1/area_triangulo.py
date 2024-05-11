from vectores import diferencia, producto_vectorial, norma

def area_triangulo(x1, y1, z1, x2, y2, z2, x3, y3, z3):
	'''Dadas las coordenadas de tres puntos devuelve el area del triangulo formado por estos'''
	vector_AB = diferencia(x2, y2, z2, x1, y1, z1)
	vector_AC = diferencia(x3, y3, z3, x1, y1, z1)
	prod_vect_ABxAC = producto_vectorial(vector_AB[0], vector_AB[1], vector_AB[2], vector_AC[0], vector_AC[1], vector_AC[2])
	norma_ABxAC = norma(prod_vect_ABxAC[0], prod_vect_ABxAC[1], prod_vect_ABxAC[2])
	area_triangulo = round(norma_ABxAC/2, 4) # para que redondee a 4 cifras
	return area_triangulo

assert area_triangulo(0,0,0,0,0,0,0,0,0) == 0.0
assert area_triangulo(0,0,0,0,1,0,0,0,1) == 0.5
assert area_triangulo(5,8,-1,-2,3,4,-3,3,0) == 19.4551 # ejemplo de la guia
assert area_triangulo(23,74,-61,3,-44,32,11,1,90) == 5596.1146