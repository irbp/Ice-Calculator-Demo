import sys, Ice
import Demo

# Ice.initialize inicia um Ice run time e retorna uma referencia ao
# Ice.Communicator que eh o objeto principal do Ice run time
with Ice.initialize(sys.argv) as communicator:
    # Obtendo o proxy do servico remoto
    base = communicator.stringToProxy('Calculadora:default -p 10000')
    
    # Retorna um proxy do tipo Demo.CalculatorPrx, caso contrario o proxy
    # eh de algum outro tipo retornando None
    calc = Demo.CalculatorPrx.checkedCast(base)
    if not calc:
        raise RuntimeError('Proxy invalido!')

    # Executando o metodo remoto
    res = calc.add(3., 2.)
    print('Resultado da soma: ', res)

    res = calc.sub(12.5, 2.75)
    print('Resultado da subtracao: ', res)

    res = calc.mul(15.43, 7.49)
    print('Resultado da multiplicacao: ', res)

    res = calc.div(-10., 4.)
    print('Resultado da divisao: ', res)