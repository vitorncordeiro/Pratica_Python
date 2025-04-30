from abc import ABC, abstractmethod

class Conta(ABC):
    """Esta classe abstrata é a classe pai dos diferentes tipos de contas"""
    def __init__(self, saldo: int | float, numeroDaConta: int | float, agencia: str):
        self._saldo = saldo
        #talvez tenha que usar getters nessas ultimas duas de baixo 
        self.agencia = agencia
        self.numeroDaConta = numeroDaConta
    @abstractmethod
    def __repr__(self):
        pass
    @property
    def saldo(self):
        return self._saldo
    @saldo.setter
    def saldo(self, saldo):
        self._saldo = saldo
    def depositar(self, valorDeDeposito: int | float):
        self._saldo += valorDeDeposito
    @abstractmethod
    def sacar(self, valorDeSaque: int | float):
        pass

class ContaPoupanca(Conta):
    def __repr__(self):
        detalhesDaConta = f'Saldo Atual: {self.saldo}'
        return detalhesDaConta
    def sacar(self, valorDeSaque: int | float):
        if self._saldo < valorDeSaque:
            print('Você não possui este saldo para saque')
        else:
            self._saldo = self._saldo - valorDeSaque
            
class ContaCorrente(Conta):
    def __init__(self, saldo, numeroDaConta, agencia, limite= 1000):
        super().__init__(saldo, numeroDaConta, agencia)
        self._limite = limite
        
        
    def __repr__(self):
        tipoDeConta = self.__class__.__name__
        detalhesDaConta = f'Tipo de conta: {tipoDeConta} | Saldo Atual: {self.saldo} | Limite atual: {self._limite} |\
 Agência: {self.agencia} | Número da Conta: {self.numeroDaConta} '
        return detalhesDaConta
    @property
    def limite(self):
        return self._limite
    @limite.setter
    def limite(self, novoValorLimite):
        self._limite = novoValorLimite
    def sacar(self, valorDeSaque: int | float):
        if self._saldo - valorDeSaque < -self.limite:
            print('Saque não autorizado: Limite ultrapassado')
        else: 
             self._saldo = self._saldo - valorDeSaque

conta1 = ContaCorrente(saldo= 20, numeroDaConta=1234, agencia="Itaú")
print(conta1)