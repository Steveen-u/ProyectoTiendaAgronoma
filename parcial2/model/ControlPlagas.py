from model.ProductoControl import ProductoControl

class ControlPlagas(ProductoControl):
    def __init__(self,nombre,precio,registroICA,frecuenciaAplicacion,periodoCarencia):
        super().__init__(nombre,precio,registroICA,frecuenciaAplicacion)
        self.__periodoCarencia = periodoCarencia

    def setPeriodoCarencia(self,periodoCarencia):
        self.__periodoCarencia=periodoCarencia

    def getPeriodoCarencia(self):
        return self.__periodoCarencia
    
    

    
