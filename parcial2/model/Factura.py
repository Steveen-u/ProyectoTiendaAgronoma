class Factura:
    def __init__(self, id, fecha, total):
        self.__id = id
        self.__fecha = fecha
        self.__total = total
        self.__productos = []
    
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self,id):
        self.__id=id

    @property
    def fecha(self):
        return self.__fecha
    
    @fecha.setter
    def fecha(self,fecha):
        self.__fecha=fecha

    @property
    def total(self):
        return self.__total

    @total.setter
    def total(self,total):
        self.__total=total

    @property
    def productos(self):
        return self.__productos

    @productos.setter
    def productos(self,producto):
        self.__productos.append(producto)


    def addAntibiotico(self,antibiotico):
        self.producto.append(antibiotico)

    def addFertilizante(self,fertilizante):
        #self.producto.append(fertilizante)
        self.productos = fertilizante

    def addPlagas(self,plagas):
        self.producto.append(plagas)