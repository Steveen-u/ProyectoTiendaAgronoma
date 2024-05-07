from model import Cliente

def registroClientes(nombre, cedula):
    cliente = Cliente.Cliente(nombre, cedula)
    return cliente

registroClientes("Juan", 1234567890)
registroClientes("Pedro", 1234567891)
registroClientes("Maria", 1234567892)