class Antibioticos:
    def __init__(self, nombre, dosis, precio, tipoAnimal):
        self.nombre = nombre
        self.dosis = dosis
        self.precio = precio
        self.tipoAnimal = tipoAnimal

    def setNombre(self, nombre):
        self.__nombre = nombre

    def getNombre(self):
        return self.__nombre
    
    def setDosis(self, dosis):
        self.__dosis = dosis

    def getDosis(self):
        return self.__dosis
    
    def setPrecio(self, precio):
        self.__precio = precio

    def getPrecio(self):
        return self.__precio
    
    def setTipoAnimal(self, tipoAnimal):
        self.__tipoAnimal = tipoAnimal

    def getTipoAnimal(self):
        return self.__tipoAnimal
    