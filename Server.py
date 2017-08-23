import sys, Ice
import Demo

class Calculator(Demo.Calculator):
    def add(self, a, b, current=None):
        return a + b

    def sub(self, a, b, current=None):
        return a - b

    def mul(self, a, b, current=None):
        return a * b

    def div(self, a, b, current=None):
        return a / b

# Ice.initialize inicia um Ice run time e retorna uma referencia ao
# Ice.Communicator que eh o objeto principal do Ice run time
with Ice.initialize(sys.argv) as communicator:
    # Cria um object adapter que ira escutar na porta 10000 utilizando o
    # protocolo TCP/IP
    adapter = communicator.createObjectAdapterWithEndpoints(
        'SimpleCalculatorAdapter', 'default -p 10000'
    )

    # Instanciando PrinterI
    object = Calculator()

    # Adicionando o servico instanciado ao adapter junto com um identificador
    # do servico que esta sendo adicionado
    adapter.add(object, communicator.stringToIdentity('Calculadora'))
    
    # Ativando o adapter
    adapter.activate()

    # Espera por uma chamada de desativacao do servidor
    communicator.waitForShutdown()