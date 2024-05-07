import unittest
from model.Cliente import Cliente
from model.Factura import Factura

class TestCliente(unittest.TestCase):

    def setUp(self):
        self.cliente = Cliente("Juan", "123456789")

    def test_nombre(self):
        # Arrange
        expected_nombre = "Pedro"

        # Act
        self.cliente.nombre = expected_nombre
        actual_nombre = self.cliente.nombre

        # Assert
        self.assertEqual(actual_nombre, expected_nombre)

    def test_cedula(self):
        # Arrange
        expected_cedula = "987654321"

        # Act
        self.cliente.cedula = expected_cedula
        actual_cedula = self.cliente.cedula

        # Assert
        self.assertEqual(actual_cedula, expected_cedula)

    def test_addFactura(self):
        # Arrange
        factura = Factura(1, "2024-04-16", 100)

        # Act
        self.cliente.addFactura(factura)

        # Assert
        self.assertIn(factura, self.cliente.facturas)

if __name__ == '__main__':
    unittest.main()
