from model.ProductoControl import ProductoControl

class ControlFertilizantes(ProductoControl):
    def __init__(self,nombre,precio,registroICA,frecuenciaAplicacion,fechaUltimaAplicacion):
        super().__init__(nombre,precio,registroICA,frecuenciaAplicacion)
        self.__fechaUltimaAplicacion = fechaUltimaAplicacion

    def setFechaUltimaAplicacion(self,fechaUltimaAplicacion):
        self.__fechaUltimaAplicacion=fechaUltimaAplicacion

    def getFechaUltimaAplicacion(self):
        return self.__fechaUltimaAplicacion
    
    