from model.Cliente import Cliente as cliente
from interfaceCrud import ICrud

class ImpCrudCliente ( ICrud . ICrud ) :

 def crear ( self , ** kwargs ) :
     return cliente.Cliente(kwargs ["name"], kwargs ["cedula"])

 def relacion ( self , ** kwargs ) :
    cliente.cuentas = kwargs [ "facturas"]
    return cliente