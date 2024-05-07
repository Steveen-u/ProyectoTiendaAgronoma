import sys
sys.path.append('../model')  # Reemplaza '/ruta/al/directorio/model' con la ruta real

# Luego puedes importar los módulos normalmente
from model.Antibioticos import Antibioticos
from model.ControlFertilizantes import ControlFertilizantes
from model.ControlPlagas import ControlPlagas

def crearProducto(tipo, nombre, precio, descripcion, cantidad, fechaVencimiento):
    if tipo == "Antibioticos":
        antibiotico = Antibioticos.Antibioticos(nombre, precio, descripcion, cantidad, fechaVencimiento)
        return antibiotico
    elif tipo == "ControlPlagas":
        controlPlaga = ControlPlagas.ControlPlagas(nombre, precio, descripcion, cantidad, fechaVencimiento)
        return controlPlaga
    elif tipo == "ControlFertilizantes":
        controlFertilizante = ControlFertilizantes.ControlFertilizantes(nombre, precio, descripcion, cantidad, fechaVencimiento)
        return controlFertilizante
    else:
        return None
    

crearProducto("Antibioticos", "Antibiotico1", 1000, "Antibiotico para vacas", 10, "2020-12-12")
crearProducto("ControlPlagas", "Plaga1", 1000, "Plaga para vacas", 10, "2020-12-12")
crearProducto("ControlFertilizantes", "Fertilizante1", 1000, "Fertilizante para vacas", 10, "2020-12-12")