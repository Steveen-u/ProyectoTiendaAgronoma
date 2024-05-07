from Factura import Factura as factura

class Cliente:
    def __init__(self,name,cedula):
        self.__name = name
        self.__cedula = cedula
        self.__facturas = []

    @property
    def nombre(self):
        return self.__name

    @nombre.setter
    def nombre(self,name):
        self.__name=name
    
    @property
    def cedula(self):
        return self.__cedula

    @cedula.setter
    def cedula(self,cedula):
        self.__cedula=cedula

    @property
    def facturas(self):
        return self.__facturas
    
    @facturas.setter
    def facturas(self,factura):
        self.__facturas.append(factura)

    def addFactura(self,factura):
        self.facturas.append(factura)