class ProductoControl:
    def __init__(self,nombre,precio,registroICA,frecuenciaAplicacion):
        self.__nombre = nombre
        self.__precio = precio
        self.__registroICA = registroICA
        self.__frecuenciaAplicacion = frecuenciaAplicacion


    def setNombre(self,nombre):
        self.__nombre=nombre

    def getNombre(self):
        return self.__nombre
    
    def setPrecio(self,precio):
        self.__precio=precio
    
    def getPrecio(self):
        return self.__precio
    
    def setRegistroICA(self,registroICA):
        self.__registroICA=registroICA

    def getRegistroICA(self):
        return self.__registroICA
    
    def setFrecuenciaAplicacion(self,frecuenciaAplicacion):
        self.__frecuenciaAplicacion=frecuenciaAplicacion

    def getFrecuenciaAplicacion(self):
        return self.__frecuenciaAplicacion
    
    