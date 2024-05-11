def billete_permitido(plata):
	for billete in plata:
		if billete not in (1,2,5,10,20,50,100,200,500,1000):
			raise ValueError(f'Denominacion "{billete}" no permitida')
	return plata 	

class Caja:

	def __init__(self, plata):
		self.plata = billete_permitido(plata)
		

	def __str__(self):
		return str(self.plata)

	def total(self):
		total = 0
		for billete, cantidad in self.plata.items():
			total += billete*cantidad
		return total

	def agregar(self, plata2):
		plata2 = billete_permitido(plata2)
		for billete, cantidad in plata2.items():
			if billete in self.plata:
				self.plata[billete] += cantidad
				continue
			self.plata[billete] = self.plata.get(billete, cantidad)
		return self.plata

    def quitar(self, menos_plata): 
        se_quito = 0
        for billete, cantidad in menos_plata.items():
            if billete not in self.plata or self.plata[billete] < cantidad:
                raise ValueError(f'No hay suficientes billetes de denominacion {billete}')
        for billete, cantidad in menos_plata.items():
            self.plata[billete] -= cantidad
            se_quito += billete*cantidad
            if self.plata[billete] == 0:
                self.plata.pop(billete)
        return se_quito



c = Caja({500: 4, 100: 7, 50: 4, 10:1})
print(c)
print(c.total())
print(c.quitar({500: 4}))
print(c)
print(c.total())