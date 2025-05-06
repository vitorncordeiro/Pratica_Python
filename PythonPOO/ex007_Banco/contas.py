from abc import ABC, abstractmethod
class Conta(ABC):
    """Esta classe abstrata é a classe pai dos diferentes tipos de contas"""
    def __init__(self, numeroDaConta: float, agencia: int, saldo: float= 0):
        self._saldo = saldo
        #talvez tenha que usar getters nessas ultimas duas de baixo 
        self.agencia = agencia
        self.numeroDaConta = numeroDaConta
    @abstractmethod
    def __repr__(self):
        pass
    @abstractmethod
    def sacar(self, valorDeSaque: float) -> float:
        pass
    @property
    def saldo(self):
        return self._saldo
    @saldo.setter
    def saldo(self, saldo):
        self._saldo = saldo
    
    def depositar(self, valorDeDeposito: float) -> float:
        self._saldo += valorDeDeposito
        return self._saldo

class ContaPoupanca(Conta):
    def __repr__(self):
        tipoDeConta = type(self).__name__
        detalhesDaConta = f'({self.numeroDaConta!r}, {self.agencia!r}, '\
            f'{self.saldo!r})'
        return f'{tipoDeConta}{detalhesDaConta}'
    def sacar(self, valorDeSaque: float):
        if self._saldo < valorDeSaque:
            print(f'Você não possui este saldo para saque: {valorDeSaque}')
        else:
            self._saldo = self._saldo - valorDeSaque
            return self._saldo
            
class ContaCorrente(Conta):
    def __init__(self, numeroDaConta, agencia, saldo= 0, limite= 0):
        super().__init__(numeroDaConta, agencia, saldo)
        self._limite = limite
        
        
    def __repr__(self):
        tipoDeConta = type(self).__name__
        detalhesDaConta = f'({self.numeroDaConta!r}, {self.agencia!r}, '\
            f'{self.saldo!r}, {self.limite!r})'
        return f'{tipoDeConta}{detalhesDaConta}'
    @property
    def limite(self):
        return self._limite
    @limite.setter
    def limite(self, novoValorLimite):
        self._limite = novoValorLimite
    def sacar(self, valorDeSaque: float):
        if self._saldo - valorDeSaque < -self.limite:
            print('Saque não autorizado: Limite ultrapassado')
        else: 
            self._saldo = self._saldo - valorDeSaque
            return self._saldo
listaContas = []
conta1 = ContaCorrente(saldo= 20, numeroDaConta=1234, agencia=43210)
conta2 = ContaCorrente(saldo= 100, numeroDaConta=123456, agencia=43210)
conta3 = ContaCorrente(saldo= 300, numeroDaConta=78910, agencia = 02468)
listaContas.append(conta1)
listaContas.append(conta2)
if __name__ == '__main__':
    
    conta1.sacar(21)
    conta2.sacar(50)
