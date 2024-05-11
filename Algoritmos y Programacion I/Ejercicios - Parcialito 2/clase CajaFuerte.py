class CajaFuerte:

    def __init__(self, codigo):
        self.codigo = codigo
        self.estado = False
        self.contenido = None

    def abrir(self, codigo_ingresado):
        if self.codigo == codigo_ingresado:
            self.estado = True
        else:
            raise Exception('La clave es inválida')

    def esta_abierta(self):
        if self.estado == True:
            return True
        return False

    def cerrar(self):
        if self.estado == True:
            self.estado = False

    def guardar(self, contenido):
        if self.contenido != None:
            raise Exception('No se puede guardar más de una cosa')
        if self.estado == False:
            raise Exception('La caja fuerte está cerrada')
        self.contenido = contenido

    def sacar(self):
        if self.estado == False:
            raise Exception('La caja fuerte está cerrada')
        if self.contenido == None:
            raise Exception('No hay nada para sacar')
        elemento, self.contenido = self.contenido, None
        return elemento

    def __str__(self):
        return str(self.contenido), str(self.estado)