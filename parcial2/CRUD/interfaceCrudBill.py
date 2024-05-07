from model.Factura import Factura as factura
from interfaceCrud import ICrud


class ImpCrudCuenta ( ICrud .ICrud ) :

 def crear ( self , ** kwargs ) :
        return factura.Factura(kwargs ["fecha"], kwargs ["total"], kwargs ["productos"])