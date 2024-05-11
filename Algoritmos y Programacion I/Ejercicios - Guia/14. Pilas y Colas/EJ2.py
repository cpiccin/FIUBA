from modelo_Cola import Cola, _Nodo

class Impresora:
	
	def __init__(self, nombre, capacidad):
		self.nombre = nombre
		self.capacidad = capacidad
		self.tinta_actual = capacidad
		self.cola_documentos = Cola()

	def imprimir(self, doc):
		if not self.cola_documentos.primero:
			print('No hay documentos encolados')
			return
		if self.tinta_actual == 0:
			print('No hay tinta')
			return
		else:
			self.tinta_actual -= 1
			print(doc)

	def cargar_tinta(self):
		if self.tinta_actual == self.capacidad:
			print('Maxima capacidad de tinta')
			return
		self.tinta_actual += 1

	def añadir_impresion(self, doc):
		self.cola_documentos.encolar(doc)




class Oficina:

	def __init__(self):
		self.impresoras = {}

	def agregar_impresora(self, impresora):
		self.impresoras[impresora.nombre] = [impresora.cola_documentos, impresora.capacidad, impresora.tinta_actual] 

	def impresora(self, nombre):
		return self.impresoras[nombre][0]

	def obtener_impresora_libre(self):
		libre = None
		for impresora in self.impresoras.items():




i1 = Impresora('casa', 250)
o = Oficina()

o.agregar_impresora(Impresora('HP1234', 1))
o.agregar_impresora(Impresora('Epson666', 5))
o.impresora('HP1234').encolar('tp1.pdf')

