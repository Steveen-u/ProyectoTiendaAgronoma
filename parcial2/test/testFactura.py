import unittest

import sys
sys.path.append('../model')  # Reemplaza '/ruta/al/directorio/model' con la ruta real

# Luego puedes importar los módulos normalmente
from model.Factura import Factura
from model.Antibioticos import Antibioticos
from model.ControlFertilizantes import ControlFertilizantes
from model.ControlPlagas import ControlPlagas

class TestFactura(unittest.TestCase):

    def setUp(self):
        self.factura = Factura(1, "2024-04-16", 100)

    def test_id(self):
        # Arrange
        expected_id = 2

        # Act
        self.factura.id = expected_id
        actual_id = self.factura.id

        # Assert
        self.assertEqual(actual_id, expected_id)

    def test_fecha(self):
        # Arrange
        expected_fecha = "2024-04-17"

        # Act
        self.factura.fecha = expected_fecha
        actual_fecha = self.factura.fecha

        # Assert
        self.assertEqual(actual_fecha, expected_fecha)

    def test_total(self):
        # Arrange
        expected_total = 200

        # Act
        self.factura.total = expected_total
        actual_total = self.factura.total

        # Assert
        self.assertEqual(actual_total, expected_total)

    def test_addAntibiotico(self):
        # Arrange
        antibiotico = Antibioticos("nombre", "dosis", "precio", "tipoAnimal")

        # Act
        self.factura.addAntibiotico(antibiotico)

        # Assert
        self.assertIn(antibiotico, self.factura.productos)

    def test_addFertilizante(self):
        # Arrange
        fertilizante = ControlFertilizantes("nombre", "precio", "registroICA", "frecuenciaAplicacion", "fechaUltimaAplicacion")

        # Act
        self.factura.addFertilizante(fertilizante)

        # Assert
        self.assertIn(fertilizante, self.factura.productos)

    def test_addPlagas(self):
        # Arrange
        plagas = ControlPlagas("nombre", "precio", "registroICA", "frecuenciaAplicacion", "periodoCarencia")

        # Act
        self.factura.addPlagas(plagas)

        # Assert
        self.assertIn(plagas, self.factura.productos)

if __name__ == '__main__':
    unittest.main()
